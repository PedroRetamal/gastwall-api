from pydantic import BaseModel, Field, field_validator

#lo que mete el usuario
class CategoriaInput(BaseModel):
    nombre: str 
    tipo: str = Field(pattern="^(ingreso|gasto)$")


class CategoriaOutput(BaseModel):
    id: int
    nombre: str
    tipo: str
    usuario_id: int

