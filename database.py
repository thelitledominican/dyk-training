import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Intentamos obtener la variable de entorno, y si no está, usamos la URL correcta del pooler de Supabase
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    # URL actualizada con el formato correcto del pooler de Supabase (puerto 5432 / 6543 y usuario con identificador)
    DATABASE_URL = "postgresql://postgres.dexyrfaoyhdudsamctqa:LavidaesbuenaDISFRUTA@aws-0-us-west-1.pooler.supabase.com:5432/postgres"

# Creamos el engine con la URL corregida
engine = create_engine(DATABASE_URL, connect_args={"connect_timeout": 10})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()