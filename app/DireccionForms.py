from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class trayectoriaForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(max=124)])
    submit = SubmitField('Regis')