from pydantic import BaseModel

#lo que mete el usuario
class CuentaInput(BaseModel):
    nombre: str


class CuentaOutput(BaseModel):
    id: int
    nombre: str
    usuario_id: int

