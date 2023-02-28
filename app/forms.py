from flask_wtf import FlaskForm
from wtforms import IntegerField,TextAreaField,SelectField,validators,StringField
from wtforms.validators import Optional, ValidationError, DataRequired

class Form(FlaskForm):
    name = StringField("name", validators=[DataRequired()])