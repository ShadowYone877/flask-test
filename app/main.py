from flask import Flask, render_template, request, redirect, url_for
from loginForm import loginForm 
from registerForm import registerForm
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField

app = Flask(__name__)
app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

@app.route("/cambiarContraseña")
def cambiarContraseña():
    return render_template("Cambiarcontraseña.html")

@app.route("/login", methods=["GET","POST"])
def login():
    form=loginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        print(email,password)
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('login'))
    return render_template("login.html",form=form)

@app.route("/asignar_comite")
def asignar_comite():
    return render_template("asignar_comite.html")

@app.route("/inicio")
def inicio():
    return render_template("inicio.html")
    
@app.route("/registro")
def registro():
    return render_template("Registro.html")

@app.route("/sesion_comite")
def sesion_comite():
    return render_template("sesion_comite.html")

@app.route("/evento")
def evento():
    return render_template("evento.html")

@app.route("/comite")
def comite():
    return render_template("comite.html")

@app.route("/tablerocomite")
def Tcomite():
    return render_template("tablerocomite.html")

@app.route("/visualizardatosu")
def mostrarDatosU():
    return render_template("visualizardatosu.html")

@app.route("/grid1")
def grid1():
    return render_template("grid1.html")

@app.route("/CerrarSesion")
def cerrarSesion():
    return render_template("cerrarsesion.html")

@app.route("/EditarDatos")
def editarDatos():
    return render_template("editardatos.html")

@app.route("/admin")
def mostrarAdmin():
    return render_template("admin.html")

@app.route("/registroForm", methods=["GET","POST"])
def registroForm():
    form=registerForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        print(name,password,email)
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('login'))
    return render_template("registroForm.html",form=form)

@app.route("/registro_usuario")
def registrousuario():
    return render_template("registrousuario.html")

@app.route("/datos")
def datos():
    return render_template("visualizarDatos.html")

@app.route("/añadir_domicilio")
def adddomicilio():
    return render_template("domicilio.html")

@app.route("/pendiente_comite")
def pendientecomite():
    return render_template("pendienteComite.html")

@app.route("/tarea", methods=["GET", "POST"])
def tarea():
    return render_template("tarea.html")

if __name__ == '__main__':
    app.run(debug=True)