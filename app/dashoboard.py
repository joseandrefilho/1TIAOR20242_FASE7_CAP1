import streamlit as st

# Módulos de cada fase
from fase1_manejo_insumos.manejo import main as manejo_main
from fase3_iot_esp32.sensores_simulados import main as sensores_main
from fase6_visao_computacional.yolov5_inferencias import exibir_resultados_yolo
from fase6_visao_computacional.cnn_inferencias import exibir_resultados_cnn
from fase4_dashboard_streamlit.dashboard import mostrar_graficos
from fase5_cloud_aws.alerta_mensageria import enviar_alerta


def main():
    # Configurações iniciais da página
    st.set_page_config(
        page_title="FarmTech Solutions - Sistema Integrado", 
        layout="wide"
    )

    st.title("FarmTech Solutions – Sistema Integrado de Gestão Agrícola")
    st.markdown(
        "Integração dos serviços das Fases 1 a 6: manejo de insumos, sensores IoT, análises preditivas, visão computacional e alertas na nuvem."
    )

    # Menu lateral para seleção de módulo
    st.sidebar.header("Módulos Disponíveis")
    modulo = st.sidebar.radio(
        "Selecione o módulo:",
        [
            "Manejo de Insumos",         # Fase 1
            "Sensores IoT",               # Fase 3
            "Análises e Previsões",       # Fase 4
            "Visão Computacional",        # Fase 6
            "Enviar Alerta AWS"           # Fase 5
        ]
    )

    st.sidebar.markdown("---")
    st.sidebar.write("© FarmTech Solutions")

    # Roteamento para cada módulo
    if modulo == "Manejo de Insumos":
        st.header("📊 Módulo de Manejo de Insumos (Fase 1)")
        manejo_main()

    elif modulo == "Sensores IoT":
        st.header("🌱 Módulo de Sensores IoT (Fase 3)")
        sensores_main()

    elif modulo == "Análises e Previsões":
        st.header("📈 Análises e Previsões (Fase 4)")
        mostrar_graficos()

    elif modulo == "Visão Computacional":
        st.header("🖥️ Visão Computacional (Fase 6)")
        st.subheader("Detecção com YOLOv5 Adaptado")
        exibir_resultados_yolo()
        st.subheader("Classificação com CNN do Zero")
        exibir_resultados_cnn()

    elif modulo == "Enviar Alerta AWS":
        st.header("🔔 Enviar Alerta (Fase 5)")
        st.write("Disparando alerta via AWS SNS...")
        enviar_alerta()
        st.success("Alerta enviado com sucesso!")


if __name__ == "__main__":
    main()
