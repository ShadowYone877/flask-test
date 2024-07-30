from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class tablerocomiteForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message="Campo email requerido")])
    password = PasswordField('Contraseña', validators=[DataRequired(message="Campo contraseña requerido")])
    submit = SubmitField('Iniciar Sesión')