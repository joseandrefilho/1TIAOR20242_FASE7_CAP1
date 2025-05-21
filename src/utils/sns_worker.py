
import requests
from db.connection import get_connection

API_URL = "https://6jgs11bi23.execute-api.eu-north-1.amazonaws.com/alerta"

def enviar_alerta_http(alerta):
    payload = {
        "umidade_id": str(alerta['cd_alerta']),
        "umidade_junto_ao_solo": alerta['ds_tipo'],
        "Valor-percentual": f"{alerta['sensor_id']:.2f}",
        "Indices": [
            {
                "Indice": f"{alerta['sensor_id']:.2f}",
                "Horario": alerta['dt_alerta'].strftime('%H')
            }
        ]
    }
    try:
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()
        print("✔️ Alerta enviado:", payload)
        return True
    except Exception as e:
        print("❌ Erro ao enviar alerta:", e)
        return False

def processar_alertas():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT cd_alerta, ds_tipo, dt_alerta, cd_sensor 
            FROM t_ssa_alertas 
            WHERE foi_enviado = 'N'
        """)
        alertas = cur.fetchall()

        for cd_alerta, ds_tipo, dt_alerta, cd_sensor in alertas:
            alerta = {
                "cd_alerta": cd_alerta,
                "ds_tipo": ds_tipo,
                "dt_alerta": dt_alerta,
                "sensor_id": float(cd_sensor) if cd_sensor else 0.0
            }
            if enviar_alerta_http(alerta):
                cur.execute("""
                    UPDATE t_ssa_alertas 
                    SET foi_enviado = 'S' 
                    WHERE cd_alerta = :1
                """, [cd_alerta])

        conn.commit()
        cur.close()
        conn.close()
        print(f"{len(alertas)} alerta(s) processado(s).")
    except Exception as e:
        print(f"Erro ao processar alertas: {e}")

if __name__ == "__main__":
    processar_alertas()
