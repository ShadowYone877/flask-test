from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class addressForm(FlaskForm):
    street = StringField('Calle', validators=[DataRequired()])
    numberExt = StringField('Numero exterior', validators=[DataRequired()])
    numberInt = StringField('Numero interior', validators=[DataRequired()])
    state = StringField('Estado:', validators=[DataRequired(), Length(max=80)])
    municipality = StringField('Municipio / Alcaldia', validators=[DataRequired()])
    cologne = StringField('Colonia', validators=[DataRequired(), Email()])
    cp = StringField('Codigo Postal', validators=[DataRequired(),Length(min=5, max=5)])
    submit = SubmitField('Siguiente')