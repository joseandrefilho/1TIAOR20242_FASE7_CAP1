CREATE DATABASE SistemaIrrigacao;

USE SistemaIrrigacao;

-- Tabela de Sensores (Detalhes das leituras)
CREATE TABLE DadosSensores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    temperatura FLOAT,              -- Captura da temperatura (DHT22)
    umidade INT,                    -- Captura da umidade do solo
    luminosidade INT,               -- Captura da luminosidade (LDR)
    distanciaAgua INT,              -- Captura do nível da água (HC-SR04)
    nutrienteP BOOLEAN,             -- Presença de nutriente P
    nutrienteK BOOLEAN,             -- Presença de nutriente K
    ph FLOAT,                       -- pH do solo
    irrigacaoAtiva BOOLEAN          -- Indicador se a irrigação está ativa
);

-- Tabela de Dispositivos (Gerenciamento dos dispositivos do sistema)
CREATE TABLE Dispositivos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,       -- Nome do dispositivo (ex: Sensor DHT22)
    tipo VARCHAR(50) NOT NULL,       -- Tipo do dispositivo (ex: Sensor, Atuador)
    localizacao VARCHAR(100)         -- Localização física do dispositivo
);

-- Tabela de Configurações do Sistema
CREATE TABLE Configuracoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    parametro VARCHAR(50) NOT NULL,  -- Nome do parâmetro (ex: LimiteUmidade)
    valor FLOAT NOT NULL,            -- Valor do parâmetro
    descricao VARCHAR(200)           -- Descrição do parâmetro
);

-- Tabela de Alertas e Logs (Monitoramento do sistema)
CREATE TABLE Logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    tipo VARCHAR(50) NOT NULL,       -- Tipo do log (ex: Alerta, Erro, Informativo)
    mensagem VARCHAR(200) NOT NULL  -- Mensagem detalhada do log
);

-- Tabela de Decisões de Irrigação (Registro das previsões e decisões do modelo)
CREATE TABLE DecisoesIrrigacao (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    temperatura FLOAT,
    umidade INT,
    luminosidade INT,
    distanciaAgua INT,
    previsaoIrrigacao BOOLEAN,       -- Previsão do modelo (1 para ON, 0 para OFF)
    mensagem VARCHAR(200)            -- Mensagem detalhada gerada pelo modelo
);
