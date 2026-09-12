import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexión directa a tu base de datos permanente en Supabase (PostgreSQL)
# Recuerda reemplazar [YOUR-PASSWORD] por la contraseña real que creaste en Supabase.
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:LavidaesbuenaDISFRUTA@db.dexyrfaoyhdudsamctqa.supabase.co:5432/postgres?sslmode=require"
# Si prefieres usar variables de entorno para mayor seguridad, puedes descomentar la siguiente línea:
# SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()