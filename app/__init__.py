from flask import Flask, render_template, request, redirect, url_for
from .loginForm import loginForm 
from .registerForm import registerForm
from .addressForm import addressForm
from .event2Form import event2Form
from .tablerocomiteForm import tablerocomiteForm
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
from .trayectoriaForm import trayectoriaForm

def create_app():
    

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
            return redirect(url_for('registro'))
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

    @app.route("/tablerocomite/", methods=["GET","POST"])
    def tablerocomite():
        form=tablerocomiteForm()
        if form.validate_on_submit():
            homework = form.homework.data
            dateinicio = form.dateinicio.data
            datefinal = form.datefinal.data
            description = form.description.data
            advance = form.advance.data
            print(homework,dateinicio,datefinal,description,advance)
            next = request.args.get('next', None)
            if next:
                return redirect(next)
            return redirect(url_for('tablerocomite'))
        return render_template("tablerocomite.html",form=form)

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
    
    @app.route("/Direccion")
    def Direccion():
        return render_template("Direccion.html")

    @app.route("/tarea", methods=["GET", "POST"])
    def tarea():
<<<<<<< HEAD
        return render_template("tarea.html") 
    
    @app.route("/address_form/", methods=["GET", "POST"])
    def address_form():
        form=addressForm()
        if form.validate_on_submit():
            street = form.street.data
            numberExt = form.numberExt.data
            numberInt = form.numberInt.data
            state = form.state.data
            municipality = form.municipality.data
            cologne = form.cologne.data
            cp = form.cp.data
            print(street, numberExt, numberInt, state, municipality, cologne, cp)
            next = request.args.get('next', None)
            if next:
                return redirect(next)
            return redirect(url_for('address_form'))
        return render_template("address_form.html",form=form)

    @app.route("/evento2/", methods=["GET","POST"])
    def segEvento():
        form=event2Form()
        if form.validate_on_submit():
            date = form.date.data
            event = form.event.data
            person = form.person.data
            print(date, event, person)
            next = request.args.get('next', None)
            if next:
                return redirect(next)
            return redirect(url_for('evento2'))
        return render_template("evento2.html", form=form)

=======
        return render_template("tarea.html")
    
    @app.route("/Trayectoria/", methods=["GET","POST"])
    def Trayectoria():
        form = trayectoriaForm()
        if form.validate_on_submit():
            name = form.name.data
            dateinicio= form.dateinicio.data
            role=form.role.data 
            print(name,dateinicio,role)
            next = request.args.get('next', None)
            if next:
                return redirect(next)
            return redirect(url_for('Trayectoria'))
        return render_template("Trayectoria.html", form=form)
    
    @app.route("/Direccion/", methods=["GET","POST"])
    def Direccion():
        form = trayectoriaForm()
        if form.validate_on_submit():
            name = form.name.data
            
            print("Pierce")
            next = request.args.get('next', None)
            if next:
                return redirect(next)
            return redirect(url_for('login'))
        return render_template("Direccion.html", form=form)
>>>>>>> 923b763 (implementacion de jinja en la vista trayectoria)

    if __name__ == '__main__':
        app.run(debug=True)
        
    return app
