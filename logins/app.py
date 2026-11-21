from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mysqldb import MySQL

app = Flask(__name__, template_folder=".")

# Configuración de la conexión
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'FlaskDB'
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.secret_key = 'mysecretkey'

mysql = MySQL(app)


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido_p = request.form["apellido_p"]
        apellido_m = request.form["apellido_m"]
        correo = request.form["correo"]
        password = request.form["password"]
        id_rol = request.form["id_rol"]

        password_hash = generate_password_hash(password)

        cursor = mysql.connection.cursor()
        cursor.execute(
            "SELECT id FROM usuarios WHERE correo = %s",
            (correo,)
        )

        if cursor.fetchone():
            cursor.close()
            return render_template(
                "registro.html",
                error="Ese correo ya está registrado"
            )

        cursor.execute("""
            INSERT INTO usuarios
            (nombre, apellido_p, apellido_m, correo, password, id_rol)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            nombre,
            apellido_p,
            apellido_m,
            correo,
            password_hash,
            id_rol
        ))

        mysql.connection.commit()
        cursor.close()

        return redirect(url_for("login"))

    return render_template("registro.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        correo = request.form["correo"]
        password = request.form["password"]

        cursor = mysql.connection.cursor()
        sql = """
            SELECT
                usuarios.id,
                usuarios.nombre,
                usuarios.apellido_p,
                usuarios.apellido_m,
                usuarios.correo,
                usuarios.password,
                roles.nombre
            FROM usuarios
            INNER JOIN roles
                ON usuarios.id_rol = roles.id_rol
            WHERE usuarios.correo = %s
        """
        cursor.execute(sql, (correo,))
        usuario = cursor.fetchone()
        cursor.close()

        if usuario and check_password_hash(usuario[5], password):
            session["id_usuario"] = usuario[0]
            session["nombre"] = usuario[1]
            session["rol"] = usuario[6]

            if session["rol"] == "Administrador":
                return redirect(url_for("admin"))
            elif session["rol"] == "Usuario":
                return redirect(url_for("usuario"))
            else:
                return "Acceso denegado", 403

        return render_template(
            "login.html",
            error="Correo o contraseña incorrectos"
        )

    return render_template("login.html")


@app.route("/admin")
def admin():
    if "id_usuario" not in session:
        return redirect(url_for("login"))

    if session.get("rol") != "Administrador":
        return "Acceso denegado", 403

    return render_template(
        "administrador.html",
        nombre=session["nombre"]
    )


@app.route("/usuario")
def usuario():
    if "id_usuario" not in session:
        return redirect(url_for("login"))

    if session.get("rol") != "Usuario":
        return "Acceso denegado", 403

    return render_template(
        "usuarios.html",
        nombre=session["nombre"]
    )


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
