import streamlit as st
from scripts import fase1_coleta, fase2_banco, fase3_iot, fase4_modelo, fase6_visao
from aws import alerta_sns

st.set_page_config(page_title="FarmTech - Fase 7", layout="wide")
st.title("🌾 Dashboard Integrada - Projeto FarmTech")

st.sidebar.title("Menu")
fase = st.sidebar.radio("Escolha a Fase", ["Fase 1", "Fase 2", "Fase 3", "Fase 4", "Fase 6"])

if fase == "Fase 1":
    st.header("☁️ Fase 1 - Meteorologia")
    if st.button("Coletar dados meteorológicos"):
        dados = fase1_coleta.obter_dados_meteorologicos()
        st.json(dados)

elif fase == "Fase 2":
    st.header("💾 Fase 2 - Banco de Dados de Sensores")
    if st.button("Criar banco"):
        fase2_banco.criar_banco()
        st.success("Banco criado.")
    if st.button("Inserir dado aleatório"):
        fase2_banco.inserir_dado("umidade", 45.2)
        st.success("Dado inserido.")
    if st.button("Listar dados"):
        dados = fase2_banco.listar_dados()
        st.write(dados)

elif fase == "Fase 3":
    st.header("🚿 Fase 3 - Simulação IoT")
    umidade = fase3_iot.simular_sensor_umidade()
    st.metric("Umidade do Solo", f"{umidade}%")
    if fase3_iot.deve_acionar_irrigacao(umidade):
        alerta_sns.enviar_alerta(f"Umidade crítica: {umidade}% - Ativar irrigação!")
        st.warning("Umidade baixa! Alerta enviado.")
    else:
        st.success("Umidade dentro dos padrões.")

elif fase == "Fase 4":
    st.header("🧠 Fase 4 - Modelo de Machine Learning")
    st.write("Insira 4 valores numéricos (ex: dados da flor Iris):")
    input_data = [st.number_input(f"Valor {i+1}", value=1.0) for i in range(4)]
    if st.button("Prever"):
        classe = fase4_modelo.prever(input_data)
        st.write(f"Classe prevista: {classe}")

elif fase == "Fase 6":
    st.header("🌿 Fase 6 - Visão Computacional (Simulada)")
    nome_img = st.text_input("Nome da imagem (ex: folha_doente.jpg):", "folha_doente.jpg")
    if st.button("Detectar praga"):
        resultado = fase6_visao.detectar_praga(nome_img)
        st.write(resultado)
