from api_flask_todo.models.usuario import Usuario
from api_flask_todo import bcrypt
from flask_jwt_extended import create_access_token

usuarios = {}  # "DB" em memória

class AuthService:
    @staticmethod
    def registrar(email: str, senha: str):
        if email in usuarios:
            return None, "Usuário já registrado"
        senha_hash = bcrypt.generate_password_hash(senha).decode("utf-8")
        usuarios[email] = Usuario(email, senha_hash)
        return usuarios[email], None

    @staticmethod
    def login(email: str, senha: str):
        user = usuarios.get(email)
      
        if not user or not bcrypt.check_password_hash(user.senha_hash, senha):
            return None
        token = create_access_token(identity=email)
        return token
