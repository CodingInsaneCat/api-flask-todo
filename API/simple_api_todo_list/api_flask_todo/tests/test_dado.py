import sys
import os

# Adiciona o diretório pai ao sys.path para encontrar o módulo utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.validators import validar_dado

def test_nao_informar_dados():
    dado = {}
    resultado = validar_dado(dado)
    assert resultado == "Nenhum dado fornecido"

def test_nao_informar_campo_de_titulo():
    dado = {"descricao": "Revisar verbos HTTP, status e boas práticas", "concluida": False}
    resultado = validar_dado(dado)
    assert resultado == "O campo 'titulo' é obrigatório"

def test_nao_informar_campo_de_descricao():
    dado = {"titulo": "Revisar verbos HTTP, status e boas práticas", "concluida": False}
    resultado = validar_dado(dado)
    assert resultado == "O campo 'descricao' é obrigatório"

def test_nao_informar_campo_de_concluido():
    dado = {"titulo": "Revisar verbos HTTP, status e boas práticas", "descricao": "testes descricao"}
    resultado = validar_dado(dado)
    assert resultado == "O campo 'concluida' é obrigatório"

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])