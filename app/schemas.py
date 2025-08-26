from pydantic import BaseModel
from typing import Optional

# Request

class UsuarioCreateRequest(BaseModel):
    username: str
    email: str

class AlumnoCreateRequest(BaseModel):
    carrera: Optional [str] = None
    usuario_id: int

# Response

class UsuarioResponse(BaseModel):
    id: int
    nombre: Optional [str]
    email: str

    class Config:
        orm_mode = True

class AlumnoResponse(BaseModel):
    id: int
    carrera: Optional [str]
    usuario: UsuarioResponse

    class Config:
        orm_mode = True