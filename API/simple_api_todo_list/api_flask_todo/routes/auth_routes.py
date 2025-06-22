from flask import Blueprint, request, jsonify
from api_flask_todo.services.auth_service import AuthService


bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/registrar", methods=["POST"])
def registrar():
    dados = request.get_json()
    email = dados.get("email")
    senha = dados.get("senha")

    if not email or not senha:
        return jsonify({"erro": "Email e senha são obrigatórios"}), 400

    usuario, erro = AuthService.registrar(email, senha)
    if erro:
        return jsonify({"erro": erro}), 400

    return jsonify({"msg": "Usuário registrado com sucesso"}), 201


@bp.route("/login", methods=["POST"])
def login():
    dados = request.get_json()
    email = dados.get("email")
    senha = dados.get("senha")

    token = AuthService.login(email, senha)
    if not token:
        return jsonify({"erro": "Credenciais inválidas"}), 401

    return jsonify({"token": token})
