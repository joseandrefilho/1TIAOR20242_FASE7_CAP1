import random

def simular_sensor_umidade():
    return random.randint(10, 100)

def deve_acionar_irrigacao(umidade):
    return umidade < 40
