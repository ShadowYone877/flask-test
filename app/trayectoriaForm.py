from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField,SelectField,DateField
from wtforms.validators import DataRequired, Email, Length


class trayectoriaForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(max=124)],render_kw={"placeholder": "Ingresa tu nombre"})
    role = SelectField('Rol', choices=[('admin', 'Administrador'), ('user', 'Usuario')], validators=[DataRequired()])
    birth_date = DateField('Fecha de Nacimiento', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Regis')