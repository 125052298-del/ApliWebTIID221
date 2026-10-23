#importamos los paquetes flask
from flask import Flask, render_template
#Creamos una instancua de nuestra aplicacion
app = Flask(__name__)
app.config['MySQL_HOST'] = 'localhost'
app.config['MySQL_USER'] = 'root'
app.config['MySQL_PASSWORD'] = ''
app.config['MySQL_DB'] = 'FlaskDB'
app.secret_key = 'mysecretkey'
app.config['TEMPLATES_AUTO_RELOAD'] = True
#permite que flask vuelva a cargar los templates cuando se realicen cambios en ellos
#creacion de la ruta /es la raiz , srra la que mostrara cusndo el proyecto se ejecute
@app.route("/")
def home():
    return render_template("login.html")
#iniciamos  el servidorFLASK en el puerto 5000
if __name__ == "__main__":
    app.run(port=5000)
