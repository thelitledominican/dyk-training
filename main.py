from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import engine, Base, SessionLocal
import models
import schemas

# NOTA: Ya no ejecutamos drop_all ni create_all aquí para evitar 
# que el servidor se congele al intentar conectar con la base de datos en el arranque.

app = FastAPI(
    title="tienda de suplementos D&K Training",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependencia para obtener la sesión de base de datos en cada petición
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"mensaje": "¡El backend de D&K Training está activo!"}

# --- RUTA POST PARA CREAR PRODUCTOS ---
@app.post("/productos/")
def crear_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    nuevo_producto = models.Producto(
        nombre=producto.nombre,
        descripcion=producto.descripcion,
        precio=producto.precio,
        imagen=producto.imagen
    )
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return nuevo_producto

# --- RUTA GET PARA LEER Y MOSTRAR LOS PRODUCTOS ---
@app.get("/productos/")
def obtener_productos(db: Session = Depends(get_db)):
    productos = db.query(models.Producto).all()
    return productos