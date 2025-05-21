from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
from db.connection import DBConnection
from datetime import datetime, timedelta

class IrrigationPredictor:
    def __init__(self):
        self.model = RandomForestClassifier(
            n_estimators=100,
            random_state=42
        )
        self.scaler = StandardScaler()
        self.is_trained = False
        
    def train(self):
        try:
            with DBConnection() as conn:
                cursor = conn.cursor()
                query = """
                    SELECT 
                        l.vl_valor_leitura as valor,
                        s.nm_sensor as sensor,
                        CASE WHEN i.cd_irrigacao IS NOT NULL THEN 1 ELSE 0 END as necessita_irrigacao
                    FROM t_ssa_leitura l
                    JOIN t_ssa_sensor s ON l.cd_sensor = s.cd_sensor
                    LEFT JOIN t_ssa_irrigacao i ON 
                        TRUNC(l.dt_leitura) = TRUNC(i.dt_irrigacao)
                        AND s.cd_cultura = i.cd_cultura
                    WHERE l.dt_leitura >= SYSDATE - 30
                    ORDER BY l.dt_leitura DESC
                """
                cursor.execute(query)
                data = cursor.fetchall()

                if not data:
                    print("Sem dados suficientes para treinar o modelo")
                    self.is_trained = False
                    return False

                # Converte para DataFrame
                df = pd.DataFrame(data, columns=['valor', 'sensor', 'necessita_irrigacao'])
                
                # Pivota o DataFrame para ter uma coluna para cada sensor
                df_pivot = df.pivot(columns='sensor', values='valor')
                df_pivot['necessita_irrigacao'] = df['necessita_irrigacao']

                # Features e target
                X = df_pivot.drop('necessita_irrigacao', axis=1)
                y = df_pivot['necessita_irrigacao']

                # Normaliza os dados
                X_scaled = self.scaler.fit_transform(X)
                
                # Treina o modelo
                self.model.fit(X_scaled, y)
                self.is_trained = True
                
                return True

        except Exception as e:
            print(f"Erro ao treinar modelo: {str(e)}")
            self.is_trained = False
            return False

    def predict_irrigation_need(self, current_data):
        try:
            if not self.is_trained:
                return {
                    'needs_irrigation': True,
                    'confidence': 0.5,
                    'feature_importance': {
                        'umidade': 0.5,
                        'temperatura': 0.3,
                        'ph': 0.2
                    }
                }

            # Prepara os dados no mesmo formato do treino
            df = pd.DataFrame([current_data])
            X_scaled = self.scaler.transform(df)
            
            # Faz a previsão
            prediction = self.model.predict(X_scaled)[0]
            probability = self.model.predict_proba(X_scaled)[0][1]
            
            return {
                'needs_irrigation': bool(prediction),
                'confidence': float(probability),
                'feature_importance': dict(zip(df.columns, self.model.feature_importances_))
            }
            
        except Exception as e:
            print(f"Erro na previsão: {str(e)}")
            return {
                'needs_irrigation': True,
                'confidence': 0.5,
                'feature_importance': {
                    'umidade': 0.5,
                    'temperatura': 0.3,
                    'ph': 0.2
                }
            }