from app import app
from flask import render_template
from app.register_form import Register
from app import db
from flask import flash, redirect, url_for
from app.models import Users, Test, Parties, Questions

@app.route('/')
def index():

    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = Register()

    if form.validate_on_submit():
        gender = form.gender.data
        age = form.age.data
        occupation = form.occupation.data
        income = form.income.data
        birthplace = form.birthplace.data
        current_city = form.current_city.data
        religion = form.religion.data

        user = Users(gender=gender, age=age, occupation=occupation, income=income, birthplace=birthplace, current_city=current_city, religion=religion)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('index'))

    else:
        return render_template('register.html', form=form)






