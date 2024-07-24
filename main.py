from flask import Flask, render_template

app = Flask(__name__)
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
    
@app.route("/registro")
def Registro():
    return render_template("Registro.html")

@app.route("/evento")
def evento():
    return render_template("evento.html")

@app.route("/comite")
def comite():
    return render_template("comite.html")

@app.route("/card")
def card():
    return render_template("card.html")

@app.route("/grid1")
def grid1():
    return render_template("grid1.html")

@app.route("/registro_usuario")
def registrousuario():
    return render_template("registrousuario.html")