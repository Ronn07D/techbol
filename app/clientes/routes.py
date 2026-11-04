from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from app.models import Cliente
from app.extensions import db

bp_clientes = Blueprint(
    "clientes",
    __name__
)


@bp_clientes.route("/")
def index():

    clientes = Cliente.query.all()

    return render_template("clientes/index.html",clientes=clientes)


@bp_clientes.route("/create", methods=["GET", "POST"])
def create():

    if request.method == "POST":

        nuevo_cliente = Cliente(
            nombre=request.form["nombre"],
            telefono=request.form["telefono"]
        )

        db.session.add(nuevo_cliente)
        db.session.commit()

        return redirect(url_for("clientes.index"))

    return render_template("clientes/create.html")


@bp_clientes.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):

    cliente = Cliente.query.get_or_404(id)

    if request.method == "POST":

        cliente.nombre = request.form["nombre"]
        cliente.telefono = request.form["telefono"]

        db.session.commit()

        return redirect(url_for("clientes.index"))

    return render_template("clientes/edit.html",cliente=cliente)


@bp_clientes.route("/delete/<int:id>")
def delete(id):

    cliente = Cliente.query.get_or_404(id)

    db.session.delete(cliente)
    db.session.commit()

    return redirect(url_for("clientes.index"))