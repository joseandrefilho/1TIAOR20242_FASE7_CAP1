
# FarmTech Solutions 🌱 - Projeto Fase 7 (FIAP 1TIAO)

Este projeto consolida todas as fases anteriores do ecossistema digital de agricultura inteligente, integrando sensores físicos, visão computacional, aprendizado de máquina e cloud computing em um único sistema operacional via dashboard.

## 🎯 Objetivo Geral
Desenvolver um sistema de gestão agrícola digital, integrando IoT, banco de dados, inteligência artificial, e envio de alertas em tempo real via AWS SNS.

## 🔁 Fases Integradas

### ✅ Fase 1 – Base de Dados Inicial
- Cálculo de área plantada
- Cadastro de culturas
- Integração com API meteorológica (para análise em R)

### ✅ Fase 2 – Banco de Dados Estruturado
- Modelo relacional completo (MER, DER)
- Scripts SQL DDL + Dados de exemplo

### ✅ Fase 3 – IoT e Automação
- Leitura de sensores simulados via Wokwi (ESP32)
- Publicação via MQTT
- Lógica de controle de irrigação automatizada

### ✅ Fase 4 – Dashboard e Machine Learning
- Previsão de irrigação com algoritmo treinado
- Visualização gráfica e geográfica com Streamlit

### ✅ Fase 5 – Cloud e Segurança
- Envio de alertas via SNS (AWS)
- Estrutura projetada para escalar e proteger dados

### ✅ Fase 6 – Visão Computacional (opcional)
- Implementação de CNN e YOLO (sem câmera física)
- Comparativo visual e arquitetural no GitHub

### ✅ Fase 7 – Consolidação do Sistema
- Interface única (`main.py`) que executa:
    - Cliente MQTT (`client.py`)
    - Dashboard Streamlit
- Geração de alertas automáticos ao detectar irrigação
- Envio imediato do alerta via HTTP para AWS SNS

## 📊 Como Executar

```bash
# Instale dependências
pip install -r requirements.txt

# Inicie o sistema completo
python src/main.py
```

## 🛰️ Envio de Alertas
- O ESP32 (via Wokwi) ativa a irrigação automaticamente
- Isso gera um alerta no banco e envia para a API SNS via HTTP
- Os alertas são exibidos no dashboard

## 📂 Estrutura de Pastas

- `mer/`: modelagem conceitual e scripts SQL
- `src/`: código-fonte principal
    - `mqtt/`: recebimento MQTT
    - `utils/`: dashboard e sns_worker (fallback)
    - `models/`, `ml/`, `db/`: lógicas específicas

## 🎥 Demonstração
[🔗 Link para o vídeo no YouTube (não listado)](https://youtube.com/seu_link_aqui)

---

> Projeto FIAP • 1TIAO • Fase 7 • Grupo FarmTech Solutions
