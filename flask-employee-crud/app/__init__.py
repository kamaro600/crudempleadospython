from flask import Flask
import os

def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.secret_key = os.getenv("SECRET_KEY", "devkey")
    app.config["DEBUG"] = os.getenv("DEBUG", "False") == "True"

    # registrar rutas
    from .routes import bp as employee_bp
    app.register_blueprint(employee_bp)

    # No crear tabla aquí: la creamos con reintentos desde run.py cuando la BD esté lista

    return app