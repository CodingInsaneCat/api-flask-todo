import re

def validar_dado(dado):
    if not dado:
        return "Nenhum dado fornecido"
    if not dado.get("titulo"):
        return "O campo 'titulo' é obrigatório"
    if not dado.get("descricao"):
        return "O campo 'descricao' é obrigatório"
    if "concluida" not in dado:
        return "O campo 'concluida' é obrigatório"
    if not isinstance(dado.get("concluida"), bool):
        return "O campo 'concluida' deve ser booleano (true/false)"
    return None


def validar_auth(dado):
    if not dado:
        return "Nenhum dado fornecido"

    email = dado.get("email", "")
    senha = dado.get("senha", "")

    if not email:
        return "O campo 'email' é obrigatório"
    
    if not senha:
        return "O campo 'senha' é obrigatório"

    # Regex simples para validar e-mail
    padrao_email = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(padrao_email, email):
        return "O campo 'email' deve ser um endereço de e-mail válido"

    if len(senha) < 6:
        return "A senha deve ter pelo menos 6 caracteres"
    
    return None