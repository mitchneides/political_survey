from flask_wtf import *
from wtforms import StringField, DateField, IntegerField, SubmitField, SelectField
from wtforms.validators import data_required


class SubmitForm(FlaskForm):
    answers = StringField()
    submit = SubmitField()
