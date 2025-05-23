import boto3
from db.connection import DBConnection

SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:820119691435:AlertaIrrigacao"  # ajuste para o seu ARN real


def enviar_alerta_sns(alerta):
    client = boto3.client('sns', region_name='us-east-1')
    mensagem = f"[Alerta {alerta['cd_alerta']}] {alerta['ds_tipo']} | Sensor ID: {alerta['sensor_id']} | Data: {alerta['dt_alerta']}"
    response = client.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=mensagem,
        Subject='🚨 Alerta FarmTech'
    )
    print("✔️ Alerta SNS enviado:", mensagem)
    print("[SNS] MessageId:", response.get('MessageId'))
    return True


def processar_alertas():
    try:
        with DBConnection() as conn:
            cur = conn.cursor()
            cur.execute("""
                SELECT cd_alerta, ds_tipo, dt_alerta, cd_sensor 
                FROM t_ssa_alertas 
                ORDER BY dt_alerta DESC
            """)
            alertas = cur.fetchall()

        for cd_alerta, ds_tipo, dt_alerta, cd_sensor in alertas:
            alerta = {
                "cd_alerta": cd_alerta,
                "ds_tipo": ds_tipo,
                "dt_alerta": dt_alerta,
                "sensor_id": float(cd_sensor) if cd_sensor else 0.0
            }
            enviar_alerta_sns(alerta)

        print(f"{len(alertas)} alerta(s) processado(s).")
    except Exception as e:
        print(f"Erro ao processar alertas: {e}")

if __name__ == "__main__":
    processar_alertas()
