class Dado:
    def __init__(self, id: int, titulo: str, descricao: str, concluida: bool):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.concluida = concluida

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "concluida": self.concluida,
        }
