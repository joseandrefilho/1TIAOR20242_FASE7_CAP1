from db.connection import DBConnection
from datetime import datetime
import boto3
from dotenv import load_dotenv
import os

load_dotenv()

SNS_TOPIC_ARN = os.getenv("SNS_TOPIC_ARN")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

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
            enviar_alerta_sns(alerta_id.getvalue(), tipo_alerta, sensor_id)
    except Exception as e:
        print(f"[ERRO] Falha ao registrar alerta: {e}")

def enviar_alerta_sns(cd_alerta, tipo_alerta, sensor_id):
    client = boto3.client('sns', region_name=AWS_REGION)
    mensagem = f"[Alerta {cd_alerta}] {tipo_alerta} | Sensor ID: {sensor_id} | Data: {datetime.now()}"
    try:
        response = client.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=mensagem,
            Subject='🚨 Alerta FarmTech'
        )
        print(f"[SNS] Alerta SNS enviado: {cd_alerta}")
        print(f"[SNS] MessageId: {response.get('MessageId')}")
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
