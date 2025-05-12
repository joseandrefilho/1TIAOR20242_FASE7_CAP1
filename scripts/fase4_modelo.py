from sklearn.ensemble import RandomForestClassifier
import pickle
import os

def carregar_modelo():
    modelo_path = "ml/modelo_random_forest.pkl"
    if os.path.exists(modelo_path):
        with open(modelo_path, "rb") as f:
            return pickle.load(f)
    else:
        return treinar_modelo_exemplo()

def treinar_modelo_exemplo():
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    iris = load_iris()
    X_train, _, y_train, _ = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)
    modelo = RandomForestClassifier()
    modelo.fit(X_train, y_train)
    with open("ml/modelo_random_forest.pkl", "wb") as f:
        pickle.dump(modelo, f)
    return modelo

def prever(input_data):
    modelo = carregar_modelo()
    return modelo.predict([input_data])[0]
