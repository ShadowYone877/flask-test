from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField,SelectField,DateField
from wtforms.validators import DataRequired, Email, Length


class trayectoriaForm(FlaskForm):
    role = SelectField('Rol', choices=[('admin', 'Administrador'), ('user', 'Usuario')], validators=[DataRequired()])
    name = StringField('nombre', validators=[DataRequired()])
    dateinicio = DateField('Fecha inicio', validators=[DataRequired()])
    
    
    submit = SubmitField('Regis')