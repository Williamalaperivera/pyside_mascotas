import os
from dotenv import load_dotenv
from alembic.config import Config
from alembic import command

def run_migrations():
    print("🚀 Iniciando migración...")
    load_dotenv()

    alembic_cfg = Config("alembic.ini")

    try:
        command.revision(alembic_cfg, autogenerate=True, message="Crear tabla mascotas")
        command.upgrade(alembic_cfg, "head")
        print("✅ Base de datos sincronizada con éxito.")
    except Exception as e:
        print(f"❌ Error durante la migración: {e}")

if __name__ == "__main__":
    run_migrations()