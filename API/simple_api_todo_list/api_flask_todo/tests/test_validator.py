import sys
import os

# Adiciona o diretório pai ao sys.path para encontrar o módulo utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.validators import validar_auth

def test_email_vazio():
    dado = {"senha": "123456"}
    resultado = validar_auth(dado)
    assert resultado == "O campo 'email' é obrigatório"

def test_email_invalido():
    dado = {"email": "invalido", "senha": "123456"}
    resultado = validar_auth(dado)
    assert resultado == "O campo 'email' deve ser um endereço de e-mail válido"

def test_email_valido_senha_curta():
    dado = {"email": "user@email.com", "senha": "123"}
    resultado = validar_auth(dado)
    assert resultado == "A senha deve ter pelo menos 6 caracteres"

def test_autenticacao_valida():
    dado = {"email": "user@email.com", "senha": "123456"}
    resultado = validar_auth(dado)
    assert resultado is None

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])