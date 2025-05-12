import streamlit as st
import pandas as pd
import plotly.express as px
import joblib
from datetime import datetime

# Carregar o modelo treinado
modelo = joblib.load("modelo_irrigacao.pkl")

# Função para ler os dados em tempo real
@st.cache_data
def ler_dados():
    try:
        return pd.read_csv("dados_irrigacao.csv")
    except FileNotFoundError:
        st.error("O arquivo 'dados_irrigacao.csv' não foi encontrado.")
        return pd.DataFrame()

# Função para realizar previsões com o modelo
def realizar_previsoes(dados):
    if dados.empty:
        return None
    # Previsão usando as colunas disponíveis
    previsoes = modelo.predict(dados[['Temperatura', 'UmidadeSolo', 'Luminosidade', 'DistanciaAgua']])
    dados["PrevisaoIrrigacao"] = previsoes
    
    # Adicionar uma coluna com mensagens descritivas
    dados["MensagemIrrigacao"] = dados["PrevisaoIrrigacao"].apply(
        lambda x: f"Irrigado às {datetime.now().strftime('%H:%M')}" if x == 1 else "Sem irrigação"
    )
    return dados

# Layout do Streamlit
st.title("Dashboard do Sistema de Irrigação")
st.sidebar.header("Opções")

# 1. Exibir dados em tempo real
st.header("📊 Dados do Sistema de Irrigação")
dados = ler_dados()
if not dados.empty:
    st.dataframe(dados)

    # Criar uma coluna de tempo baseada no índice
    dados["tempo"] = range(len(dados))

    # Gráficos interativos
    st.subheader("Variação da Umidade do Solo")
    graf_umidade = px.line(dados, x="tempo", y="UmidadeSolo", title="Umidade do Solo ao longo do tempo")
    st.plotly_chart(graf_umidade, use_container_width=True)

    st.subheader("Variação da Luminosidade")
    graf_luminosidade = px.line(dados, x="tempo", y="Luminosidade", title="Luminosidade ao longo do tempo")
    st.plotly_chart(graf_luminosidade, use_container_width=True)

    st.subheader("Distância do Nível de Água")
    graf_distancia = px.bar(dados, x="tempo", y="DistanciaAgua", title="Distância do Nível de Água")
    st.plotly_chart(graf_distancia, use_container_width=True)

# 2. Previsões do modelo de Machine Learning
st.header("🧠 Insights do Modelo de Machine Learning")
if not dados.empty:
    st.subheader("Previsões de Ativação da Irrigação")
    dados_com_previsoes = realizar_previsoes(dados)
    if dados_com_previsoes is not None:
        st.dataframe(dados_com_previsoes[["Temperatura", "UmidadeSolo", "Luminosidade", 
                                          "DistanciaAgua", "MensagemIrrigacao"]])
        st.success("Previsões realizadas com sucesso!")

# 3. Exportar os dados
st.header("💾 Exportar Dados")
if st.button("Exportar Dados para CSV"):
    dados.to_csv("dados_irrigacao_exportados.csv", index=False)
    st.success("Dados exportados com sucesso! Nome do arquivo: dados_irrigacao_exportados.csv")
