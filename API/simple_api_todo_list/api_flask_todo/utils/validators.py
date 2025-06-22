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
