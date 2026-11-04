from flask import Blueprint

bp_pedidos = Blueprint(
    "pedidos",
    __name__
)

@bp_pedidos.route("/")
def index():
    return "Modulo Pedidos"