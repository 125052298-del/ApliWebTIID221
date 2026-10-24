#importamos los paquetes flask
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['MySQL_HOST'] = 'localhost'
app.config['MySQL_USER'] = 'root'
app.config['MySQL_PASSWORD'] = ''
app.config['MySQL_DB'] = 'FlaskDB'
app.secret_key = 'mysecretkey'
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route("/", methods=["GET", "POST"])
def home():
    message = None
    if request.method == "POST":
        message = "El inicio de sesión todavía no está conectado a una base de datos."

    return render_template("login.html", message=message)


@app.route("/registro", methods=["GET", "POST"])
def registro():
    message = None
    if request.method == "POST":
        required_fields = (
            "nombre",
            "apellido_p",
            "apellido_m",
            "correo",
            "password",
            "id_rol",
        )
        if any(not request.form.get(field, "").strip() for field in required_fields):
            message = "Completa todos los campos del formulario de registro."
        else:
            message = "El registro todavía no está conectado a una base de datos; no se guardaron los datos."

    return render_template("login.html", message=message)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
