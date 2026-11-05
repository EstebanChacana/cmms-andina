import os
import sqlite3
import uuid
from flask import Flask, render_template, request, redirect, url_for, flash

BASE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(BASE, "cmms.db")
SCHEMA = os.path.join(BASE, "..", "database", "schema.sql")
FOTOS = os.path.join(BASE, "static", "fotos")

app = Flask(__name__)
app.secret_key = "cmms-andina-dev"


def db():
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    return con


def init_db():
    os.makedirs(FOTOS, exist_ok=True)
    con = db()
    with open(SCHEMA, encoding="utf-8") as f:
        con.executescript(f.read())
    con.commit()
    con.close()


# ---------- HU-001: Registro de activos ----------
@app.route("/")
@app.route("/activos")
def activos():
    con = db()
    lista = con.execute("SELECT * FROM activos ORDER BY id DESC").fetchall()
    con.close()
    return render_template("activos.html", activos=lista)


@app.route("/activos/nuevo", methods=["GET", "POST"])
def activo_nuevo():
    if request.method == "POST":
        f = request.form
        con = db()
        try:
            con.execute(
                "INSERT INTO activos (codigo, nombre, tipo, marca, modelo, ubicacion, criticidad) "
                "VALUES (?,?,?,?,?,?,?)",
                (f["codigo"].strip(), f["nombre"].strip(), f["tipo"], f["marca"],
                 f["modelo"], f["ubicacion"], f["criticidad"]),
            )
            con.commit()
            flash("Activo registrado correctamente.")
            return redirect(url_for("activos"))
        except sqlite3.IntegrityError:
            flash("Ya existe un activo con ese código.")
        finally:
            con.close()
    return render_template("activo_form.html")


# ---------- HU-003a: Reporte de falla con foto ----------
@app.route("/reportar", methods=["GET", "POST"])
def reportar():
    con = db()
    if request.method == "POST":
        f = request.form
        nombre_foto = None
        foto = request.files.get("foto")
        if foto and foto.filename:
            ext = os.path.splitext(foto.filename)[1].lower()
            nombre_foto = uuid.uuid4().hex + ext
            foto.save(os.path.join(FOTOS, nombre_foto))
        con.execute(
            "INSERT INTO reportes_falla (activo_id, reportado_por, descripcion, criticidad, foto) "
            "VALUES (?,?,?,?,?)",
            (f["activo_id"], f["reportado_por"], f["descripcion"], f["criticidad"], nombre_foto),
        )
        con.commit()
        con.close()
        flash("Falla reportada correctamente.")
        return redirect(url_for("reportes"))
    lista = con.execute("SELECT id, codigo, nombre FROM activos ORDER BY nombre").fetchall()
    con.close()
    return render_template("reportar.html", activos=lista)


@app.route("/reportes")
def reportes():
    con = db()
    lista = con.execute(
        "SELECT r.*, a.nombre AS activo, a.codigo FROM reportes_falla r "
        "JOIN activos a ON a.id = r.activo_id ORDER BY r.id DESC"
    ).fetchall()
    con.close()
    return render_template("reportes.html", reportes=lista)


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
