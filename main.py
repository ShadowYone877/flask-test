from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def hello():
    return render_template("datosu.html")

@app.route("/CambiarContraseña")
def CambiarContraseña():
    return render_template("CambiarContraseña.html")

@app.route("/login")
def Vistalogin():
    return render_template("login.html")