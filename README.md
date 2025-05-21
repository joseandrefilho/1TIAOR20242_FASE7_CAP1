
# 🌱 FarmTech - Projeto Fase 7 (FIAP)

## 📘 Descrição
Sistema integrado de gestão agrícola com suporte a IoT, Machine Learning, Visão Computacional e Cloud Computing (AWS), consolidando as entregas das Fases 1 a 6.

## 🚀 Funcionalidades por Fase

- **Fase 1**: Coleta meteorológica simulada (temperatura, umidade, chuva).
- **Fase 2**: Armazenamento de sensores em banco SQLite com visualização.
- **Fase 3**: Simulação de sensores de umidade e controle automatizado da irrigação.
- **Fase 4**: Visualização interativa com Streamlit e modelo preditivo (ML).
- **Fase 5**: Envio de alertas por e-mail (AWS SNS) com base em anomalias.
- **Fase 6**: Visão computacional (simulada) para detecção de pragas agrícolas.

## 🧰 Tecnologias Usadas

- Python 3.10+
- Streamlit
- SQLite
- scikit-learn (Random Forest)
- AWS SNS (mock e instrução real)
- Simulação de YOLO/CNN

## ▶️ Como Executar

1. Instale dependências:
```bash
pip install -r requirements.txt
```

2. Rode a dashboard:
```bash
streamlit run dash/app.py
```

## 📡 Alerta AWS SNS (mock)
O alerta está simulado via print. Para produção:

- Crie um tópico SNS na AWS
- Configure credenciais (via AWS CLI ou `~/.aws/credentials`)
- Atualize o ARN no arquivo `aws/alerta_sns.py`

## 🖼️ Prints e Arquitetura

- Arquitetura geral: `docs/arquitetura.png`
- Exemplo da dashboard: `docs/prints_dashboard.png`

## 🎥 Vídeo de Demonstração
[Coloque aqui o link do vídeo não listado no YouTube]

