import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Obtenemos la URL de la base de datos desde las variables de entorno de Render (Supabase)
DATABASE_URL = os.getenv("DATABASE_URL")

# Si por alguna razón no la encuentra localmente, puedes dejar una de respaldo, 
# pero en producción Render usará la variable de entorno.
if not DATABASE_URL:
    DATABASE_URL = "postgresql://postgres:LavidaesbuenaDISFRUTA@aws-0-us-west-1.pooler.supabase.com:5432/postgres"

# Creamos el engine único con su respectivo timeout de seguridad
engine = create_engine(DATABASE_URL, connect_args={"connect_timeout": 10})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()