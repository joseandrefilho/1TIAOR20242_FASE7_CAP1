import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import time
import os
from datetime import datetime, timedelta

from db.connection import DBConnection
from models.sensor import Sensor
from models.leitura import Leitura
from models.irrigacao import Irrigacao
from models.cultura import Cultura
from ml.predictor import IrrigationPredictor
from models.alerta import listar_alertas

st.set_page_config(
    page_title="FarmTech Solutions Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

@st.cache_resource
def load_model():
    try:
        predictor = IrrigationPredictor()
        success = predictor.train()
        if not success:
            st.warning("Não foi possível treinar o modelo com dados históricos. Usando previsões padrão.")
        return predictor
    except Exception as e:
        st.error(f"Erro ao carregar modelo: {str(e)}")
        return IrrigationPredictor()

def get_latest_readings():
    with DBConnection() as conn:
        cursor = conn.cursor()
        query = """
            SELECT 
                s.nm_sensor,
                l.vl_valor_leitura,
                l.dt_leitura,
                s.vl_latitude_sensor,
                s.vl_longitude_sensor,
                s.cd_sensor
            FROM t_ssa_leitura l
            JOIN t_ssa_sensor s ON l.cd_sensor = s.cd_sensor
            WHERE l.dt_leitura >= (SYSTIMESTAMP - INTERVAL '1' HOUR)
                AND s.nm_sensor IN ('umidadeSolo', 'temperatura', 'pH', 'nutrienteP', 'nutrienteK')
            ORDER BY l.dt_leitura DESC
        """
        cursor.execute(query)
        columns = [desc[0] for desc in cursor.description]
        data = cursor.fetchall()
        return pd.DataFrame(data, columns=columns)

def get_historical_data(days=7):
    with DBConnection() as conn:
        cursor = conn.cursor()
        query = """
            SELECT 
                l.dt_leitura,
                s.nm_sensor,
                l.vl_valor_leitura,
                c.nm_cultura
            FROM t_ssa_leitura l
            JOIN t_ssa_sensor s ON l.cd_sensor = s.cd_sensor
            JOIN t_ssa_cultura c ON s.cd_cultura = c.cd_cultura
            WHERE l.dt_leitura >= :start_date
                AND s.nm_sensor IN ('umidadeSolo', 'temperatura', 'pH', 'nutrienteP', 'nutrienteK')
            ORDER BY l.dt_leitura DESC
        """
        start_date = datetime.now() - timedelta(days=days)
        cursor.execute(query, [start_date])
        columns = [desc[0] for desc in cursor.description]
        data = cursor.fetchall()
        return pd.DataFrame(data, columns=columns)

def get_irrigation_events(days=7):
    with DBConnection() as conn:
        cursor = conn.cursor()
        query = """
            SELECT 
                i.dt_irrigacao,
                i.vl_quantidade_agua_aplicada,
                c.nm_cultura
            FROM t_ssa_irrigacao i
            JOIN t_ssa_cultura c ON i.cd_cultura = c.cd_cultura
            WHERE i.dt_irrigacao >= :start_date
            ORDER BY i.dt_irrigacao DESC
        """
        start_date = datetime.now() - timedelta(days=days)
        cursor.execute(query, [start_date])
        columns = [desc[0] for desc in cursor.description]
        data = cursor.fetchall()
        return pd.DataFrame(data, columns=columns)

predictor = load_model()

st.sidebar.title("Controles")
days_to_show = st.sidebar.slider("Período de Análise (dias)", 1, 30, 7)
update_interval = st.sidebar.slider("Intervalo de Atualização (s)", 5, 60, 30)

aba = st.sidebar.radio("Navegar", ["Dashboard", "Alertas"])

if aba == "Dashboard":
    st.title("FarmTech Solutions - Dashboard")
    col1, col2, col3 = st.columns(3)
    latest_data = get_latest_readings()

    sensors_display = [
        ('umidadeSolo', 'Umidade do Solo', '%'),
        ('temperatura', 'Temperatura', '°C'),
        ('pH', 'pH', '')
    ]

    for col, (sensor_key, label, unit) in zip([col1, col2, col3], sensors_display):
        with col:
            try:
                value = float(latest_data[latest_data['NM_SENSOR'] == sensor_key]['VL_VALOR_LEITURA'].iloc[0])
                st.metric(label=label, value=f"{value:.1f}{unit}")
            except:
                st.metric(label=label, value="N/A")

    st.subheader("Previsão de Irrigação")
    if not latest_data.empty:
        current_data = {}
        missing_data = []
        sensor_id = None

        required_sensors = {
            'umidadeSolo': ('umidadeSolo', 'Umidade do Solo'),
            'temperatura': ('temperatura', 'Temperatura'),
            'pH': ('pH', 'pH'),
            'nutrienteP': ('nutrienteP', 'Nutriente P'),
            'nutrienteK': ('nutrienteK', 'Nutriente K')
        }

        for sensor_key, (model_key, display_name) in required_sensors.items():
            sensor_data = latest_data[latest_data['NM_SENSOR'] == sensor_key]
            if not sensor_data.empty:
                valor = float(sensor_data['VL_VALOR_LEITURA'].iloc[0])
                current_data[model_key] = valor
                sensor_id = int(sensor_data['CD_SENSOR'].iloc[0])
                st.success(f"✅ {display_name}: {valor:.2f}")
            else:
                missing_data.append(display_name)
                st.error(f"❌ {display_name}: Sem dados")

        # Garante a ordem das features igual ao fit do modelo
        feature_order = ['umidadeSolo', 'temperatura', 'pH', 'nutrienteP', 'nutrienteK']
        current_data_ordered = {k: current_data[k] for k in feature_order if k in current_data}
        if len(current_data_ordered) == len(feature_order):
            df = pd.DataFrame([current_data_ordered], columns=feature_order)
            prediction = predictor.predict_irrigation_need(df.iloc[0].to_dict())
        else:
            st.warning("⚠️ Previsão indisponível: dados faltantes.")
            st.write("Dados faltantes:")
            for sensor in missing_data:
                st.write(f"- {sensor}")
            prediction = None

        if prediction:
            pred_col1, pred_col2 = st.columns(2)

            with pred_col1:
                if prediction['needs_irrigation']:
                    st.error("🚨 Necessidade de Irrigação Detectada!")
                else:
                    st.success("✅ Níveis de Irrigação Adequados")
                st.metric("Confiança da Previsão", f"{prediction['confidence']:.1%}")

            with pred_col2:
                st.write("Importância dos Fatores:")
                importances = pd.DataFrame(
                    prediction['feature_importance'].items(), 
                    columns=['Fator', 'Importância']
                ).sort_values('Importância', ascending=False)
                st.dataframe(importances)
        else:
            st.warning("⚠️ Previsão indisponível")
            st.write("Dados faltantes:")
            for sensor in missing_data:
                st.write(f"- {sensor}")

    tab1, tab2, tab3 = st.tabs(["Visão Geral", "Histórico", "Mapa"])

    with tab1:
        st.subheader("Últimas Leituras")
        if not latest_data.empty:
            st.dataframe(latest_data.sort_values('DT_LEITURA', ascending=False), hide_index=True)
        st.subheader("Eventos de Irrigação Recentes")
        irrigation_data = get_irrigation_events(days=days_to_show)
        if not irrigation_data.empty:
            st.dataframe(irrigation_data, hide_index=True)

    with tab2:
        st.subheader("Histórico de Leituras")
        # Define required_sensors para uso neste escopo
        required_sensors = {
            'umidadeSolo': ('umidade', 'Umidade do Solo'),
            'temperatura': ('temperatura', 'Temperatura'),
            'pH': ('ph', 'pH'),
            'nutrienteP': ('nutriente_p', 'Nutriente P'),
            'nutrienteK': ('nutriente_k', 'Nutriente K')
        }
        historical_data = get_historical_data(days=days_to_show)
        for sensor_key, (_, display_name) in required_sensors.items():
            sensor_data = historical_data[historical_data['NM_SENSOR'] == sensor_key]
            if not sensor_data.empty:
                fig = px.line(sensor_data, x='DT_LEITURA', y='VL_VALOR_LEITURA', title=f'Histórico - {display_name}')
                st.plotly_chart(fig, use_container_width=True)

    with tab3:
        st.subheader("Localização dos Sensores")
        if not latest_data.empty:
            fig_map = px.scatter_map(
                latest_data,
                lat='VL_LATITUDE_SENSOR',
                lon='VL_LONGITUDE_SENSOR',
                color='NM_SENSOR',
                hover_data=['VL_VALOR_LEITURA'],
                zoom=15,
                height=600
            )
            fig_map.update_layout(mapbox_style='open-street-map')
            st.plotly_chart(fig_map, use_container_width=True)

    if st.sidebar.checkbox("Atualização Automática", True):
        time.sleep(update_interval)
        st.rerun()
    if st.sidebar.button("Atualizar Dados"):
        st.rerun()

elif aba == "Alertas":
    st.title("🔔 Histórico de Alertas")
    alertas = listar_alertas(limit=20)
    if alertas:
        st.table(alertas)
    else:
        st.info("Nenhum alerta registrado.")
