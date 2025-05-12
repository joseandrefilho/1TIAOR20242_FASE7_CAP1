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

# Função para inserir dados
def inserir_dados(umidade, nutrienteP, nutrienteK, ph, irrigacaoAtiva):
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        sql = """INSERT INTO DadosSensores (umidade, nutrienteP, nutrienteK, ph, irrigacaoAtiva)
                 VALUES (%s, %s, %s, %s, %s)"""
        valores = (umidade, nutrienteP, nutrienteK, ph, irrigacaoAtiva)
        cursor.execute(sql, valores)
        conexao.commit()
        cursor.close()
        conexao.close()
        print("Dados inseridos com sucesso!")

# Função para ler dados
def ler_dados():
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM DadosSensores ORDER BY timestamp DESC LIMIT 10")
        registros = cursor.fetchall()
        for registro in registros:
            print(registro)
        cursor.close()
        conexao.close()
