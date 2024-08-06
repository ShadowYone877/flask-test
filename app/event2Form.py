from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired, Length

class event2Form(FlaskForm):
    date = DateField('Fecha:', validators=[DataRequired()])
    event = StringField('Evento', validators=[DataRequired(), Length(max=50)])
    person = StringField('Persona', validators=[DataRequired(), Length(max=50)])
    submit = SubmitField('siguiente')