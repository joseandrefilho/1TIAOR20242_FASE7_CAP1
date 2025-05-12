def detectar_praga(nome_arquivo):
    if "doente" in nome_arquivo.lower():
        return "⚠️ Praga detectada na folha."
    return "✅ Nenhuma praga identificada."
