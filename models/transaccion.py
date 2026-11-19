from pydantic import BaseModel
from datetime import datetime

#lo que mete el usuario
class TransaccionInput(BaseModel):
    monto: float
    descripcion: str
    categoria_id: int
    cuenta_id: int

#lo que sale para ver 
class TransaccionOutput(BaseModel):
    id: int
    monto: float
    descripcion: str
    fecha: datetime
    categoria_id: int
    cuenta_id: int
    usuario_id: int
