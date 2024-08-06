from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired, Length


class tablerocomiteForm(FlaskForm):
    homework = StringField('Tarea asignada', validators=[DataRequired()])
    dateinicio = DateField('Fecha inicio', validators=[DataRequired()])
    datefinal = DateField('Fecha final', validators=[DataRequired()])
    description = StringField('Descripcion', validators=[DataRequired(), Length(max=80)])
    advance = StringField('Avance', validators=[DataRequired()])
    submit = SubmitField('cargar')