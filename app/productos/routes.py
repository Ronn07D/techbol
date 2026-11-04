from flask import Blueprint

bp_productos = Blueprint(
    "productos",
    __name__
)

@bp_productos.route("/")
def index():
    return "Modulo Productos"