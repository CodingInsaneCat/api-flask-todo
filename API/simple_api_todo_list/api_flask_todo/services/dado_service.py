from api_flask_todo.models.dado import Dado

class DadoService:
    def __init__(self):
        self._dados = []
        self._id_contador = 1

    def adicionar_dado(self, titulo: str, descricao: str, concluida: bool) -> Dado:
        dado = Dado(self._id_contador, titulo, descricao, concluida)
        self._dados.append(dado)
        self._id_contador += 1
        return dado

    def listar_dados(self):
        return self._dados

    def buscar_por_id(self, id: int):
        for dado in self._dados:
            if dado.id == id:
                return dado
        return None

dado_service = DadoService()
