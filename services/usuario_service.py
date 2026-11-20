import bcrypt
from repositories.usuario_repository import UsuarioRepository
from services.auth_service import AuthService
from exceptions import UsuarioYaExisteError, CredencialesInvalidasError

class UsuarioService:
    def __init__(self, repositorio: UsuarioRepository, auth_service: AuthService):
        self.repo = repositorio
        self.auth_service = auth_service

    def registrar(self, username: str, password: str):
        obtener = self.repo.obtener_por_username(username)
        if obtener:
            raise UsuarioYaExisteError("El usuario ya existe")
        #ahora hashear contraseña
        salt = bcrypt.gensalt()
        password_bytes = password.encode("utf-8")
        password_hash = bcrypt.hashpw(password_bytes, salt)
        password_str = password_hash.decode("utf-8")
        return self.repo.crear(username,password_str)


    def verificar_credenciales(self, username: str, password: str):
        usuario = self.repo.obtener_por_username(username)
        if not usuario:
            return None
        password_hash = password.encode("utf-8")
        password_usuario_hash = usuario.password_hash.encode("utf-8")

        if not bcrypt.checkpw(password_hash, password_usuario_hash):
            return None
        return usuario
        

    def login(self, username: str, password: str):
        usuario = self.verificar_credenciales(username, password)

        if not usuario:
            raise CredencialesInvalidasError("Credenciales inválidas")
        
        return self.auth_service.generar_token(usuario)