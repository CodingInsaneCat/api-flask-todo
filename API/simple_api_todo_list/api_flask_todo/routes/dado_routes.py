from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from api_flask_todo.services.dado_service import dado_service
from api_flask_todo.utils.validators import validar_dado

bp = Blueprint("dados", __name__, url_prefix="/dados")

@bp.route("/", methods=["POST"])
@jwt_required()
def inserir_dado():
    """
    Insere um novo dado
    ---
    tags:
      - Dados
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            titulo:
              type: string
            descricao:
              type: string
            concluida:
              type: boolean
    responses:
      201:
        description: Dado inserido com sucesso
      400:
        description: Erro de validação
    """
    dados = request.get_json()

    erro = validar_dado(dados)
    if erro:
        return jsonify({"error": erro}), 400

    novo_dado = dado_service.adicionar_dado(
        titulo=dados["titulo"], descricao=dados["descricao"], concluida=dados["concluida"]
    )

    return jsonify({"message": "Dados inseridos com sucesso", "dados": novo_dado.to_dict()}), 201


@bp.route("/", methods=["GET"])
@jwt_required()
def listar_dados():
    lista = [d.to_dict() for d in dado_service.listar_dados()]
    return jsonify({"dados": lista}), 200


@bp.route("/<int:id>", methods=["GET"])
@jwt_required()
def consultar_dado_por_id(id):
    dado = dado_service.buscar_por_id(id)
    if not dado:
        return jsonify({"error": "Dado não encontrado"}), 404
    return jsonify({"dados": dado.to_dict()}), 200
