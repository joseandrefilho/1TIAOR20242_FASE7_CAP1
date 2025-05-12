import sqlite3

def criar_banco():
    conn = sqlite3.connect("data/farmtech.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sensores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT NOT NULL,
            valor REAL NOT NULL,
            data TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def inserir_dado(tipo, valor):
    conn = sqlite3.connect("data/farmtech.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO sensores (tipo, valor) VALUES (?, ?)", (tipo, valor))
    conn.commit()
    conn.close()

def listar_dados():
    conn = sqlite3.connect("data/farmtech.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sensores ORDER BY data DESC")
    dados = cursor.fetchall()
    conn.close()
    return dados
