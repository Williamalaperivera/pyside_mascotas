import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Cargar variables de entorno
load_dotenv()

# Credenciales
user = os.getenv("DB_USER")
password = os.getenv("DB_PASS")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
name = os.getenv("DB_NAME")

# URL conexión MySQL
DATABASE_URL = f"mysql+pymysql://{user}:{password}@{host}:{port}/{name}"

# Motor de conexión
engine = create_engine(DATABASE_URL)

# Sesiones
Session = sessionmaker(bind=engine)

# Base para modelos
Base = declarative_base()

# Prueba de conexión
if __name__ == "__main__":
    try:
        with engine.connect() as connection:
            print("✅ ¡Conexión exitosa a MySQL!")
            print(connection)
    except Exception as e:
        print("❌ Error al conectar a la base de datos:")
        print(e)