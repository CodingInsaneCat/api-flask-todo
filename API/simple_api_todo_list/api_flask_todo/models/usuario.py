class Usuario:
    def __init__(self, email: str, senha_hash: str):
        self.email = email
        self.senha_hash = senha_hash
