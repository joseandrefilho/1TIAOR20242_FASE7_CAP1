import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# 1. Carregar os dados
dados = pd.read_csv('scripts/dados_irrigacao.csv')

# Features (dados de entrada)
X = dados[['Temperatura', 'UmidadeSolo', 'Luminosidade', 'DistanciaAgua']]

# Target (variável de saída)
y = dados['Irrigacao'].apply(lambda x: 1 if x == 'ON' else 0)  # Converter 'ON' para 1 e 'OFF' para 0

# 2. Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Treinar o modelo (Random Forest)
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# 4. Validar o modelo
y_pred = modelo.predict(X_test)
print("Acurácia do modelo:", accuracy_score(y_test, y_pred))

# 5. Salvar o modelo treinado
joblib.dump(modelo, 'scripts/modelo_irrigacao.pkl')
print("Modelo salvo como 'modelo_irrigacao.pkl'")
