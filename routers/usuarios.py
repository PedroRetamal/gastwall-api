from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.usuario import UsuarioInput, UsuarioOutput, LoginInput, TokenOutput
from database_sqlalchemy import SessionLocal, get_db
from repositories.usuario_repository import UsuarioRepository
from services.usuario_service import UsuarioService
from services.auth_service import AuthService
from exceptions import UsuarioYaExisteError, CredencialesInvalidasError


router = APIRouter()

#registro
@router.post("/registro", response_model=UsuarioOutput, status_code=201)
def registrar_usuario(datos: UsuarioInput, db: Session = Depends(get_db)):
    repo = UsuarioRepository(db)
    auth_service = AuthService()
    servicio = UsuarioService(repo, auth_service)

    try:
        nuevo_usuario = servicio.registrar(datos.username, datos.password)
    except UsuarioYaExisteError as error:
        #usuario duplicado pero pasarlo a http
        raise HTTPException(status_code=400, detail=str(error))
    return nuevo_usuario

@router.post("/login", response_model=TokenOutput)
def login(datos: LoginInput, db: Session = Depends(get_db)):
    repo = UsuarioRepository(db)
    auth_service = AuthService()
    servicio = UsuarioService(repo, auth_service)

    try:
        usuario = servicio.login(datos.username, datos.password)
    except CredencialesInvalidasError as error:
        raise HTTPException(status_code=401, detail=str(error))
    return usuario