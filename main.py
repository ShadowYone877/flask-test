from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("inicio.html")

@app.route("/datosusuario")
def hello():
    return render_template("datosu.html")

@app.route("/CambiarContraseña")
def CambiarContraseña():
    return render_template("CambiarContraseña.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/inicio")
def inicio():
    return render_template("inicio.html")
    
@app.route("/Registro")
def Registro():
    return render_template("Registro.html")

@app.route("/evento")
def evento():
    return render_template("evento.html")

@app.route("/comite")
def comite():
    return render_template("comite.html")