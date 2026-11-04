from flask import Blueprint

bp_clientes = Blueprint(
    "clientes",
    __name__
)

@bp_clientes.route("/")
def index():
    return "Modulo Clientes"