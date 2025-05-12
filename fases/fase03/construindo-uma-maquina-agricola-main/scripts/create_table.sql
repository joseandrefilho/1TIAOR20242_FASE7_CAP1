CREATE DATABASE SistemaIrrigacao;

USE SistemaIrrigacao;

CREATE TABLE DadosSensores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    umidade INT,
    nutrienteP BOOLEAN,
    nutrienteK BOOLEAN,
    ph INT,
    irrigacaoAtiva BOOLEAN
);