import pandas as pd
from api import ler_dados

# Exportar dados para CSV
def exportar_para_csv():
    df = ler_dados()
    df.to_csv("dados_irrigacao.csv", index=False)
    print("Dados exportados para dados_irrigacao.csv")

exportar_para_csv()
