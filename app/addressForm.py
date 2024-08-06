from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length


class addressForm(FlaskForm):
    street = StringField('Calle', validators=[DataRequired(message='Campo requerido')])
    numberExt = StringField('Numero exterior', validators=[DataRequired(message='Campo requerido')])
    numberInt = StringField('Numero interior', validators=[DataRequired(message='Campo requerido')])
    state = StringField('Estado:', validators=[DataRequired(message='Campo requerido'), Length(max=80)])
    municipality = StringField('Municipio / Alcaldia', validators=[DataRequired(message='Campo requerido')])
    cologne = StringField('Colonia', validators=[DataRequired(message='Campo requerido')])
    cp = StringField('Codigo Postal', validators=[DataRequired(message='Campo requerido'),Length(min=5, max=5, message='Requiere este campo minimo 5 numeros')])
    submit = SubmitField('Siguiente')