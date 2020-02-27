from flask_wtf import *
from wtforms import StringField, DateField, IntegerField, SubmitField, SelectField
from wtforms.validators import data_required


class Register(FlaskForm):
    gender = SelectField('Gender', choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other'), ('X', 'Prefer not to say')], validators=[data_required()])
    age = IntegerField(label="Age", validators=[data_required()])
    occupation = StringField('Occupation', validators=[data_required()])
    income = SelectField('Monthly Income', choices=[('U', 'Unemployed'), ('3', '0-3,000'), ('6', '3,001-6,500'), ('9', '6,501-9,000'), ('12', '9,001-12,500'), ('16', '12,501-16,000'), ('19', '16,001-19,500'), ('A', 'Above 19,500'), ('X', 'Prefer not to say')])
    birthplace = StringField('Birthplace', validators=[data_required()])
    current_city = StringField('Current City', validators=[data_required()])
    religion = SelectField('Religious Affiliation', choices=[('N', 'None'), ('J', 'Judaism'), ('I', 'Islam'), ('C', 'Christianity'), ('H', 'Hinduism'), ('B', 'Buddhism'), ('S', 'Sikhism'), ('A', 'Atheism'), ('X', 'Prefer not to say')], validators=[data_required()])
    submit = SubmitField()
