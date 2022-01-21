from flask import Flask, render_template

app = Flask(__name__)


@app.route("/play/<numero>/<color>", methods = ["GET"])
def paginaInicial(numero, color):
    return render_template("index.html", numero=int(numero), color=color)

@app.errorhandler(404)
def paginaNoEncontrada(error):
    return "¡Lo siento! No hay respuesta. Inténtalo mas tarde"

if __name__ == "__main__":
    app.run(debug=True)