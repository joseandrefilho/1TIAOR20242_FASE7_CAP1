def obter_dados_meteorologicos():
    import random
    return {
        "temperatura": round(random.uniform(20.0, 35.0), 1),
        "umidade": round(random.uniform(30.0, 90.0), 1),
        "chuva_prevista": random.choice([True, False])
    }
