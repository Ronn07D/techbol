from flask import Flask

from config import Config
from app.extensions import db
from app.extensions import migrate

from app.clientes.routes import bp_clientes
from app.productos.routes import bp_productos
from app.pedidos.routes import bp_pedidos


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    migrate.init_app(app, db)

    app.register_blueprint(
        bp_clientes,
        url_prefix="/clientes"
    )

    app.register_blueprint(
        bp_productos,
        url_prefix="/productos"
    )

    app.register_blueprint(
        bp_pedidos,
        url_prefix="/pedidos"
    )

    @app.route("/")
    def inicio():
        return "Bienvenido a TechBol"

    return app