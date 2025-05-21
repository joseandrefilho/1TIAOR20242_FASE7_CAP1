from db.connection import DBConnection
from datetime import datetime

def registrar_alerta(sensor_id: int, tipo_alerta: str):
    """
    Insere um novo alerta na tabela T_SSA_ALERTAS.
    """
    try:
        with DBConnection() as conn:
            cur = conn.cursor()
            insert_query = """
                INSERT INTO T_SSA_ALERTAS (cd_alerta, ds_tipo, dt_alerta, cd_sensor)
                VALUES (T_SSA_ALERTAS_SEQ.NEXTVAL, :1, :2, :3)
            """
            cur.execute(insert_query, (tipo_alerta, datetime.now(), sensor_id))
            conn.commit()
            cur.close()
            print(f"[ALERTA] Registrado: '{tipo_alerta}' (sensor {sensor_id})")
    except Exception as e:
        print(f"[ERRO] Falha ao registrar alerta: {e}")

def listar_alertas(limit=10):
    """
    Retorna os últimos alertas registrados, ordenados por data decrescente.
    """
    try:
        with DBConnection() as conn:
            cur = conn.cursor()
            query = f"""
                SELECT cd_alerta, ds_tipo, dt_alerta, cd_sensor
                FROM T_SSA_ALERTAS
                ORDER BY dt_alerta DESC
                FETCH FIRST {limit} ROWS ONLY
            """
            cur.execute(query)
            rows = cur.fetchall()
            cur.close()

        # Converte em dicionários
        alertas = [
            {
                "Código": row[0],
                "Tipo": row[1],
                "Data/Hora": row[2],
                "Sensor": row[3]
            }
            for row in rows
        ]
        return alertas
    except Exception as e:
        print(f"[ERRO] Falha ao listar alertas: {e}")
        return []
