from flask import Blueprint
from flask import render_template

from app.models import Producto

from flask import request
from flask import redirect
from flask import url_for

from app.extensions import db

bp_productos = Blueprint("productos",__name__)

@bp_productos.route("/")
def index():

    productos = Producto.query.all()

    return render_template("productos/index.html",productos=productos)

@bp_productos.route('/create', methods=['GET', 'POST'])
def create():

    if request.method == 'POST':

        nuevo_producto = Producto(
            nombre=request.form['nombre'],
            precio=request.form['precio'],
            stock=request.form['stock']
        )

        db.session.add(nuevo_producto)

        db.session.commit()

        return redirect(
            url_for('productos.index')
        )

    return render_template('productos/create.html')

@bp_productos.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):

    producto = Producto.query.get_or_404(id)

    if request.method == "POST":

        producto.nombre = request.form["nombre"]
        producto.precio = request.form["precio"]
        producto.stock = request.form["stock"]

        db.session.commit()

        return redirect(
            url_for("productos.index")
        )

    return render_template("productos/edit.html",producto=producto)

@bp_productos.route("/delete/<int:id>")
def delete(id):

    producto = Producto.query.get_or_404(id)

    db.session.delete(producto)

    db.session.commit()

    return redirect(url_for("productos.index"))