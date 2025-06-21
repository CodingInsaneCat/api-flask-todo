from flask import jsonify, request
from flask import Flask
from collections import OrderedDict


app = Flask(__name__)

dados_lista = []
id_contador = 1

@app.route('/dados', methods=['POST'])
def inserir_dados():
    global id_contador
    dados = request.get_json()

    # Validadores DE CAMPOS DA APLICAÇÃO
    if dados == None or len(dados) == 0 or dados == {}:
        return jsonify({"error": "Nenhum dado fornecido"}), 400
    if dados.get('titulo') is None or dados.get('titulo') == '':
        return jsonify({"error": "O campo 'titulo' é obrigatório"}), 400
    if dados.get('descricao') is None or dados.get('descricao') == '':
        return jsonify({"error": "O campo 'descricao' é obrigatório"}), 400
    if dados.get('concluida') is None or dados.get('concluida') == '' :
        return jsonify({"error": "O campo 'concluida' é obrigatório"}), 400
    if not isinstance(dados.get('concluida'), bool):
        return jsonify({"error": "O campo 'concluida' deve ser booleano (true/false)"}), 400
    if not request.is_json:
        return jsonify({"error": "O corpo da requisição deve ser JSON"}), 415
    
    dados_ordenados = OrderedDict([
        ('id', id_contador),
        ('titulo', dados['titulo']),
        ('descricao', dados['descricao']),
        ('concluida', dados['concluida'])
    ])
    id_contador += 1
    dados_lista.append(dados_ordenados)
    print("dados_lista:", dados_lista)
    # Retorna os dados inseridos com sucesso
    # e o status HTTP 201 (Created)
    print("Dados inseridos com sucesso:", dados_ordenados)    
    
    return jsonify({
        "message": "Dados inseridos com sucesso",
        "dados": dados_ordenados
    }), 201


@app.route('/consultar-dados/', methods=['GET'])
def consultar_dados():
    # Retorna todos os dados inseridos
    return jsonify({"dados": dados_lista}), 200

@app.route('/consultar-dados-id/<int:id>', methods=['GET'])
def consultar_dados_por_id(id):
    if not isinstance(id, int):
        return jsonify({"error": "ID deve ser um número inteiro"}), 400
    if id < 1 or id == None or id == "":
        return jsonify({"error": "ID inválido"}), 400
    if id > len(dados_lista):
        return jsonify({"error": "ID fora do intervalo"}), 400
    if id != int(id):
        return jsonify({"error": "ID deve ser um número inteiro"}), 400
    # Busca o dado pelo ID
    for dado in dados_lista:
        if dado['id'] == id:
            return jsonify({"dados": dado}), 200
    
    # Se não encontrar, retorna erro 404
    return jsonify({"error": "Dado não encontrado"}), 404
if __name__ == '__main__':
    app.run(debug=True)