from db.connection import DBConnection
from datetime import datetime
import requests

API_URL = "https://6jgs11bi23.execute-api.eu-north-1.amazonaws.com/alerta"

def registrar_alerta(sensor_id: int, tipo_alerta: str, enviar: bool = True):
    """
    Grava um alerta no banco e envia imediatamente via SNS se 'enviar' for True.
    """
    try:
        with DBConnection() as conn:
            cur = conn.cursor()
            insert_query = """
                INSERT INTO T_SSA_ALERTAS (cd_alerta, ds_tipo, dt_alerta, cd_sensor)
                VALUES (T_SSA_ALERTAS_SEQ.NEXTVAL, :1, :2, :3)
                RETURNING cd_alerta INTO :4
            """
            alerta_id = cur.var(int)
            cur.execute(insert_query, (
                tipo_alerta,
                datetime.now(),
                sensor_id,
                alerta_id
            ))
            conn.commit()
            cur.close()
        print(f"[ALERTA] Gravado: {tipo_alerta} (sensor {sensor_id})")
        if enviar:
            enviar_alerta_http(alerta_id.getvalue(), tipo_alerta, sensor_id)
    except Exception as e:
        print(f"[ERRO] Falha ao registrar alerta: {e}")

def enviar_alerta_http(cd_alerta, tipo_alerta, sensor_id):
    """
    Envia o alerta via HTTP para a API da AWS.
    """
    payload = {
        "umidade_id": str(cd_alerta),
        "umidade_junto_ao_solo": tipo_alerta,
        "Valor-percentual": f"{sensor_id:.2f}",
        "Indices": [
            {
                "Indice": f"{sensor_id:.2f}",
                "Horario": datetime.now().strftime('%H')
            }
        ]
    }
    try:
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()
        print(f"[SNS] Alerta enviado: {cd_alerta}")
        print(f"[SNS] Status code: {response.status_code}")
        print(f"[SNS] Response body: {response.text}")
        return True
    except Exception as e:
        print(f"[ERRO] Falha ao enviar alerta SNS: {e}")
        return False

def listar_alertas(limit=10):
    """
    Retorna os últimos alertas registrados, ordenados por data decrescente.
    """
    try:
        with DBConnection() as conn:
            cur = conn.cursor()
            query = f"""
                SELECT ds_tipo, dt_alerta
                FROM T_SSA_ALERTAS
                ORDER BY dt_alerta DESC
                FETCH FIRST {limit} ROWS ONLY
            """
            cur.execute(query)
            rows = cur.fetchall()
            cur.close()
        alertas = [
            {
                "Tipo": row[0],
                "Data/Hora": row[1]
            }
            for row in rows
        ]
        return alertas
    except Exception as e:
        print(f"[ERRO] Falha ao listar alertas: {e}")
        return []
