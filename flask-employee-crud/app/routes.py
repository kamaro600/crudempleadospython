from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Employee

bp = Blueprint("employees", __name__, url_prefix="/")

@bp.route("/")
def index():
    items = Employee.all()
    return render_template("index.html", employees=items)

@bp.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        position = request.form.get("position", "").strip()
        if not (username and name and email and position):
            flash("Todos los campos son obligatorios", "warning")
            return redirect(url_for(".create"))
        try:
            emp = Employee.create(username, name, email, position)
            flash("Empleado creado", "success")
            return redirect(url_for(".index"))
        except Exception as e:
            flash(str(e), "danger")
            return redirect(url_for(".create"))
    return render_template("form.html", action="Crear", employee=None)

@bp.route("/<int:id>")
def detail(id):
    emp = Employee.get(id)
    if not emp:
        flash("Empleado no encontrado", "warning")
        return redirect(url_for(".index"))
    return render_template("detail.html", employee=emp)

@bp.route("/<int:id>/edit", methods=["GET", "POST"])
def edit(id):
    emp = Employee.get(id)
    if not emp:
        flash("Empleado no encontrado", "warning")
        return redirect(url_for(".index"))
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        position = request.form.get("position", "").strip()
        if not (username and name and email and position):
            flash("Todos los campos son obligatorios", "warning")
            return redirect(url_for(".edit", id=id))
        try:
            Employee.update(id, username, name, email, position)
            flash("Empleado actualizado", "success")
            return redirect(url_for(".index"))
        except Exception as e:
            flash(str(e), "danger")
            return redirect(url_for(".edit", id=id))
    return render_template("form.html", action="Editar", employee=emp)

@bp.route("/<int:id>/delete", methods=["POST"])
def delete(id):
    Employee.delete(id)
    flash("Empleado eliminado", "success")
    return redirect(url_for(".index"))