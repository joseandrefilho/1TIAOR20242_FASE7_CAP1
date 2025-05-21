import sys
import os
from db.connection import DBConnection
import boto3

def enviar_alerta_sns(mensagem):
    client = boto3.client('sns', region_name='us-east-1')
    response = client.publish(
        TopicArn='arn:aws:sns:us-east-1:123456789012:FarmTechAlerta',
        Message=mensagem,
        Subject='🚨 Alerta FarmTech'
    )
    print("Alerta enviado:", response['MessageId'])

def processar_alertas():
    try:
        with DBConnection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT cd_alerta, ds_tipo, dt_alerta, cd_sensor 
                FROM t_ssa_alertas 
                WHERE foi_enviado = 'N'
            """)
            alertas = cursor.fetchall()

            for cd_alerta, ds_tipo, dt_alerta, cd_sensor in alertas:
                mensagem = f"[{dt_alerta}] ALERTA: {ds_tipo} | Sensor ID: {cd_sensor}"
                enviar_alerta_sns(mensagem)

                cursor.execute("""
                    UPDATE t_ssa_alertas 
                    SET foi_enviado = 'S' 
                    WHERE cd_alerta = :1
                """, [cd_alerta])

            conn.commit()
            cursor.close()
        print(f"{len(alertas)} alerta(s) processado(s).")
    except Exception as e:
        print(f"Erro ao processar alertas: {e}")

if __name__ == "__main__":
    processar_alertas()
