import mysql.connector
from mysql.connector import Error

# Função para conectar ao banco de dados
def conectar():
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            user='seu_usuario',
            password='sua_senha',
            database='SistemaIrrigacao'
        )
        return conexao
    except Error as e:
        print(f"Erro na conexão: {e}")
        return None

# Função para inserir dados nos sensores
def inserir_dados_sensores(temperatura, umidade, luminosidade, distanciaAgua, nutrienteP, nutrienteK, ph, irrigacaoAtiva):
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        sql = """INSERT INTO DadosSensores 
                 (temperatura, umidade, luminosidade, distanciaAgua, nutrienteP, nutrienteK, ph, irrigacaoAtiva)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        valores = (temperatura, umidade, luminosidade, distanciaAgua, nutrienteP, nutrienteK, ph, irrigacaoAtiva)
        cursor.execute(sql, valores)
        conexao.commit()
        cursor.close()
        conexao.close()
        print("Dados dos sensores inseridos com sucesso!")

# Função para inserir decisões de irrigação
def inserir_decisao_irrigacao(temperatura, umidade, luminosidade, distanciaAgua, previsaoIrrigacao, mensagem):
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        sql = """INSERT INTO DecisoesIrrigacao 
                 (temperatura, umidade, luminosidade, distanciaAgua, previsaoIrrigacao, mensagem)
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        valores = (temperatura, umidade, luminosidade, distanciaAgua, previsaoIrrigacao, mensagem)
        cursor.execute(sql, valores)
        conexao.commit()
        cursor.close()
        conexao.close()
        print("Decisão de irrigação inserida com sucesso!")

# Função para ler os últimos dados dos sensores
def ler_dados_sensores():
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM DadosSensores ORDER BY timestamp DESC LIMIT 10")
        registros = cursor.fetchall()
        for registro in registros:
            print(registro)
        cursor.close()
        conexao.close()

# Função para ler as últimas decisões de irrigação
def ler_decisoes_irrigacao():
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM DecisoesIrrigacao ORDER BY timestamp DESC LIMIT 10")
        registros = cursor.fetchall()
        for registro in registros:
            print(registro)
        cursor.close()
        conexao.close()

# Função para registrar um log
def registrar_log(tipo, mensagem):
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        sql = """INSERT INTO Logs (tipo, mensagem) VALUES (%s, %s)"""
        valores = (tipo, mensagem)
        cursor.execute(sql, valores)
        conexao.commit()
        cursor.close()
        conexao.close()
        print("Log registrado com sucesso!")
