from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField
from wtforms.validators import DataRequired, Length

class eventForm(FlaskForm):
    date = DateField('Fecha:', validators=[DataRequired()])
    percentage = SelectField('Porcentaje', validators=[DataRequired()])
    state = SelectField('Estado', validators=[DataRequired()])
    submit = SubmitField('Enviar')
    township = StringField('Municipio/Alcaldía', validators=[DataRequired(), Length(max=100)])