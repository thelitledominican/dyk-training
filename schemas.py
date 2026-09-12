from pydantic import BaseModel

class ProductoCreate(BaseModel):
    nombre: str
    descripcion: str | None = None
    precio: float
    imagen: str | None = None