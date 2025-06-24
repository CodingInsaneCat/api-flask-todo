from flask import Flask, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flasgger import Swagger

bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    swagger_template = {
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "JWT Authorization header using the Bearer scheme. Example: 'Authorization: Bearer {token}'"
        }
    },
    "security": [{"Bearer": []}]
}

    swagger = Swagger(app, template=swagger_template)
    app.config.from_object("api_flask_todo.config.Config")


    bcrypt.init_app(app)
    jwt.init_app(app)

    # Importa blueprints e registra
    from api_flask_todo.routes.auth_routes import bp as auth_bp
    from api_flask_todo.routes.dado_routes import bp as dado_bp


    app.register_blueprint(auth_bp)
    app.register_blueprint(dado_bp)

    # Handlers personalizados JWT
    @jwt.unauthorized_loader
    def custom_unauthorized_response(err_msg):
        return jsonify({'erro': 'Token ausente ou inválido'}), 401

    @jwt.expired_token_loader
    def custom_expired_token_response(jwt_header, jwt_payload):
        return jsonify({'erro': 'Token expirado'}), 401

    @jwt.invalid_token_loader
    def custom_invalid_token_response(err_msg):
        return jsonify({'erro': 'Token inválido'}), 401

    return app
