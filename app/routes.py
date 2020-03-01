from app import app
from flask import render_template
from app.register_form import Register
from app.survey_form import SubmitForm
from app import db
from flask import flash, redirect, url_for, request
from app.models import Users, Test, Parties, Questions
import datetime
from app.compare_functions import *

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


@app.route('/survey', methods=['GET', 'POST'])
def survey():
    if request.method == 'GET':
        questions = Questions.query.all()
        form = SubmitForm()
        pretend_data = [1,2,3,4,5]

        return render_template('survey.html', questions=questions, pretend_data=pretend_data, form=form)

    if request.method == 'POST':
        form = SubmitForm(request.form)

        # push user answers to db
        answer_string = form.answers.data
        last_user_id = Users.query.order_by(Users.id.desc()).first().id

        # run comparisons
        party_answers = Parties.query.all()
        scores_with_each_party = []
        for answer in party_answers:
            party_answer_as_list = answer.answers.split(',')
            user_answer_as_list = answer_string.split(",")
            score = compare_two_score_lists(user_answer_as_list, party_answer_as_list)
            scores_with_each_party.append((answer.id, score))

        sorted_scores = sort_tuple(scores_with_each_party)
        top_party = sorted_scores[0][0]
        second_party = sorted_scores[1][0]
        third_party = sorted_scores[2][0]

        test = Test(date=datetime.datetime.now(), answers=answer_string, user_id=last_user_id, party_1_id=top_party, party_2_id=second_party, party_3_id=third_party)
        db.session.add(test)
        db.session.commit()

        return redirect('results.html')


    #         return render_template('survey.html', form=form)



        # survey.add_event_listeners();       /////////doesnt work but need to find way to access the result list(string) from js
        # user_answer = survey.submit_button()
        # print(user_answer)

    #     pull user answers from post request and party answers from db
    #     run comparrison logic





