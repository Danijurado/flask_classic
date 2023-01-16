from datetime import date
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, FloatField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

class MovementsForm(FlaskForm):
     date = DateField('Fecha', validators=[DataRequired(message='campo obligatorio')])
     concept = StringField('Concepto', validators=[DataRequired(message='campo obligatorio'), Length(min=4)])
     quantity = FloatField('cantidad', validators=[DataRequired(message='campo obligatorio')])
     
     submit = SubmitField('Aceptar')
     def validate_date(form,field):
        if field.data > date.today():
            raise ValidationError("fecha invalida")
      
 
     