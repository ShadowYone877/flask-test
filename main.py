from flask import Flask, render_template, request, redirect, url_for
from registerForm import registerForm
app = Flask(__name__)
app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

@app.route("/CambiarContraseña")
def CambiarContraseña():
    return render_template("cambiarcontraseña.html")

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

@app.route("/visualizardatosu")
def mostrarDatosU():
    return render_template("visualizardatosu.html")

@app.route("/grid1")
def grid1():
    return render_template("grid1.html")

@app.route("/grid2")
def grid2():
    return render_template("grid2.html")

@app.route("/CerrarSesion")
def cerrarSesion():
    return render_template("cerrarsesion.html")

@app.route("/EditarDatos")
def editarDatos():
    return render_template("editardatos.html")

@app.route("/Admin")
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

if __name__ == '__main__':
    app.run(debug=True)
