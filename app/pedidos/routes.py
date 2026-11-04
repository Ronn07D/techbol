from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from app.models import Pedido
from app.models import Cliente
from app.models import Producto

from app.extensions import db

bp_pedidos = Blueprint(
    "pedidos",
    __name__
)


@bp_pedidos.route("/")
def index():

    pedidos = Pedido.query.all()

    return render_template("pedidos/index.html",pedidos=pedidos)


@bp_pedidos.route("/create", methods=["GET", "POST"])
def create():

    clientes = Cliente.query.all()
    productos = Producto.query.all()

    if request.method == "POST":

        nuevo_pedido = Pedido(
            monto=request.form["monto"],
            cliente_id=request.form["cliente_id"],
            producto_id=request.form["producto_id"]
        )

        db.session.add(nuevo_pedido)
        db.session.commit()

        return redirect(url_for("pedidos.index"))

    return render_template("pedidos/create.html",clientes=clientes,productos=productos)

@bp_pedidos.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):

    pedido = Pedido.query.get_or_404(id)

    clientes = Cliente.query.all()
    productos = Producto.query.all()

    if request.method == "POST":

        pedido.cliente_id = request.form["cliente_id"]
        pedido.producto_id = request.form["producto_id"]
        pedido.monto = request.form["monto"]

        db.session.commit()

        return redirect(url_for("pedidos.index"))

    return render_template("pedidos/edit.html",pedido=pedido,clientes=clientes,productos=productos)

@bp_pedidos.route("/delete/<int:id>")
def delete(id):

    pedido = Pedido.query.get_or_404(id)

    db.session.delete(pedido)
    db.session.commit()

    return redirect(url_for("pedidos.index"))
