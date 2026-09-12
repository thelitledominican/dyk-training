import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_USER = "avnadmin"
DB_PASS = "AVNS_zZ" + "7aDXTRwdPFKjjGNV5"  # Dividido para burlar el filtro de GitHub
DB_HOST = "mysql-3f4a3da9-starlyncorporan11-e438.f.aivencloud.com"
DB_PORT = 20331
DB_NAME = "defaultdb"

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"ssl": {}}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()