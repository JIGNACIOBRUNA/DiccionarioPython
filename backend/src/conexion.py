import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

def conexion():
    try:
        connection = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_DATABASE')
        )
        
        print("Conexion exitosa")
        return connection
    except Exception as ex:
        print(ex)
        return None

conection = conexion()    