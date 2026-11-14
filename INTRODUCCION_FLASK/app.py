#Importamos paquetes de flask
from flask import Flask, flash, render_template, request, redirect, session, url_for

#importacion para generar hash y comprobar si la contra coincide con el hash
from werkzeug.security import check_password_hash, generate_password_hash

from flask_mysqldb import MySQL

#Creamos instancia de la app
app = Flask(__name__)

#Configuracion de la conexion
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskdb'
app.secret_key = 'mysecretkey'
mysql = MySQL (app)



#RUTA

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/iniciar-sesion", methods=["POST"])
def iniciar_sesion():
    correo = request.form["correo"]
    password = request.form["password"]
    cursor = mysql.connection.cursor()
    cursor.execute(
        "SELECT id, nombre, password FROM usuarios WHERE correo = %s",
        (correo,),
    )
    usuario = cursor.fetchone()
    cursor.close()

    if not usuario or not check_password_hash(usuario[2], password):
        flash("El correo o la contraseña no son correctos.", "error")
        return redirect(url_for("home"))

    session["usuario_id"] = usuario[0]
    session["usuario_nombre"] = usuario[1]
    flash("Sesión iniciada correctamente.", "success")
    return redirect(url_for("home"))

@app.route("/cerrar-sesion")
def cerrar_sesion():
    session.clear()
    flash("La sesión se cerró correctamente.", "success")
    return redirect(url_for("home"))

@app.route("/registro", methods=["GET", "POST"])
def registro():

    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido_p = request.form["apellido_p"]
        apellido_m = request.form["apellido_m"]
        correo = request.form["correo"]
        password_hash = request.form["password"]
        id_rol = request.form["id_rol"]

        password = generate_password_hash(password_hash)

        cursor = mysql.connection.cursor()

        cursor.execute(
            "SELECT id FROM usuarios WHERE correo = %s",
            (correo,),
        )
        if cursor.fetchone():
            cursor.close()
            flash("Ya existe una cuenta registrada con ese correo.", "error")
            return redirect(url_for("registro"))

        cursor.execute(
            """INSERT INTO usuarios
            (nombre, apellido_p, apellido_m, correo, password, id_rol)
            VALUES (%s, %s, %s, %s, %s, %s)""",
            (
                nombre,
                apellido_p,
                apellido_m,
                correo,
                password,
                id_rol,
            ),
        )

        mysql.connection.commit()
        cursor.close()
        flash("Cuenta creada correctamente. Ya puedes iniciar sesión.", "success")
        return redirect(url_for("home"))

    return render_template("registro.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    #Recuperamos correo y contraseña
    if request.method == "POST":
        correo = request.form["correo"]
        password = request.form["password"]
        #creamks el cursor para ejecutar la consulta SQL
        cursor = mysql.connection.cursor()
        #consukta oara buscar el usuario por correo
        sql = """
SELECT
usuarios.id,
usuarios.nombre,
usuarios.apellido_p,
usuarios.apellido_m,
usuarios.correo,
usuarios.password,
roles.nombre,
FROM usuarios
INNER JOIN id_rol
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

            if session[6] == "administrador":
                return redirect(url_for("admin"))
            return redirect(url_for("usuario"))

    return render_template("login.html")

#ruta de administrador
@app.route("/admin")
def admin():
    if "id_usuario" not in session:
        return redirect(url_for("login"))
    if session.get("rol") != "Administrador":
        return "Acceso denegado"
    return render_template("admnistrador.html", nombre=session["nombre"])

#Iniciamos servidor Flask en el puerto 5000
if __name__ == "__main__":
    app.run(port=5000)
