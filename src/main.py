import threading
import sys
import os
from mqtt.client import MQTTClient
import subprocess

def run_mqtt():
    # Instancia o cliente MQTT e inicia a escuta
    mqtt_client = MQTTClient()
    mqtt_client.start()

def run_streamlit():
    # Ajusta o caminho para encontrar o dashboard.py na pasta src
    dashboard_path = os.path.join(os.path.dirname(__file__), 'dashboard.py')
    # Usa subprocess para rodar o Streamlit
    subprocess.Popen(['streamlit', 'run', dashboard_path])

def main():
    # Inicia MQTT em uma thread separada
    mqtt_thread = threading.Thread(target=run_mqtt)
    mqtt_thread.daemon = True
    mqtt_thread.start()

    # Inicia Streamlit e aguarda o processo
    dashboard_path = os.path.join(os.path.dirname(__file__), 'dashboard.py')
    try:
        proc = subprocess.Popen(['streamlit', 'run', dashboard_path])
        proc.wait()
    except KeyboardInterrupt:
        print("Encerrando o programa...")
        proc.terminate()
        proc.wait()

if __name__ == "__main__":
    main()