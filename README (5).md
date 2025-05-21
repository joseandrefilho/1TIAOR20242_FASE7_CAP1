
# 🌿 FarmTech Solutions - Projeto Fase 7 (FIAP - 1TIAO)

Este repositório contém a consolidação de todas as fases anteriores do projeto de Agricultura Inteligente, incluindo IoT, banco de dados, machine learning, visão computacional e integração com AWS.

---

## 🎯 Objetivo Geral

Integrar sensores simulados, banco de dados, predição de irrigação e envio de alertas via AWS SNS em uma solução centralizada de gestão agrícola digital.

---

## 🔁 Fases Integradas

### Fase 1 – Base Inicial
- Cadastro de culturas e área plantada
- Integração com API meteorológica
- Cálculo de área por cultura

### Fase 2 – Banco Relacional
- MER e DER
- Scripts SQL (DDL + dados de amostra)

### Fase 3 – IoT
- Simulação via ESP32 (Wokwi)
- Leitura de sensores (DHT22, LDR, botões)
- Publicação via MQTT
- Acionamento automático de irrigação

### Fase 4 – Dashboard e ML
- Streamlit com métricas em tempo real
- Previsão de necessidade de irrigação (Scikit-Learn)
- Visualização em mapa, histórico e gráfico

### Fase 5 – Cloud & Segurança
- Envio de alertas em tempo real via API SNS
- Estrutura escalável para cloud (AWS)

### Fase 6 – Visão Computacional
- YOLO e CNN (com imagens estáticas)
- Comparações visuais de precisão e arquitetura

### Fase 7 – Consolidação Final
- Execução centralizada (`main.py`)
- Geração e envio de alertas automáticos (sem interação manual)
- Integração de todas as fases anteriores

---

## 🚀 Como Executar o Projeto

```bash
# Instalar dependências
pip install -r requirements.txt

# Executar sistema completo
python src/main.py
```

---

## 🛰️ Funcionamento do Alerta SNS

- Quando a irrigação é ativada pelo ESP32 (`IRR == 1`), um alerta é automaticamente:
  - Gravado no banco (`T_SSA_ALERTAS`)
  - Enviado para a API da AWS SNS via HTTP POST
  - Marcado como enviado (`foi_enviado = 'S'`)

---

## 📁 Estrutura de Pastas

| Pasta | Conteúdo |
|-------|----------|
| `src/` | Código principal (dashboard, mqtt, modelos, ml) |
| `mer/` | Modelagem de dados e scripts SQL |
| `utils/` | Dashboard e ferramentas auxiliares |
| `mqtt/` | Cliente MQTT com lógica de negócio |
| `models/` | Classes de domínio: leitura, cultura, sensor, alerta |
| `ml/` | Previsão com Scikit-Learn |
| `db/` | Conexão com banco Oracle ou SQLite |
| `main.py` | Inicia dashboard + MQTT simultaneamente |

---

## 🎥 Vídeo de Apresentação

🔗 [Clique aqui para assistir no YouTube (modo não listado)](https://youtube.com/seu_link_aqui)

---

## 📚 Tecnologias Utilizadas

- Python 3.10
- Streamlit
- Scikit-Learn
- SQLite / Oracle
- MQTT (via `paho-mqtt`)
- AWS SNS (via API Gateway)
- Wokwi (ESP32 virtual)

---

## 👨‍🌾 Integrantes

- [Seu nome]
- [Outros membros do grupo, se houver]

---

> FIAP • 1TIAO • Fase 7 • FarmTech Solutions 🌱
