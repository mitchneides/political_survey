from app import app
from flask import render_template
from app.register_form import Register
from app.survey_form import SubmitForm
from app import db
from flask import flash, redirect, url_for, request
from app.models import Users, Test, Parties, Questions
import datetime
from app.compare_functions import *
from plotly import graph_objs as go


@app.route('/')
def index():
    return render_template('index.html')


# sends user registration info to db and takes user to survey
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

        user = Users(gender=gender, age=age, occupation=occupation, income=income, birthplace=birthplace,
                     current_city=current_city, religion=religion)

        db.session.add(user)
        db.session.commit()
        return redirect('survey')

    else:
        return render_template('register.html', form=form)


# loads survey, pushes user answers to db, runs comparison between user and party answers
@app.route('/survey', methods=['GET', 'POST'])
def survey():
    if request.method == 'GET':
        questions = Questions.query.all()
        form = SubmitForm()
        return render_template('survey.html', questions=questions, form=form)

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

        # defines top 3 matching parties and the scores compared to each
        sorted_scores = sort_tuple(scores_with_each_party)
        print(sorted_scores)
        first_party_id = sorted_scores[0][0]
        party_1_score = sorted_scores[0][1]
        second_party_id = sorted_scores[1][0]
        party_2_score = sorted_scores[1][1]
        third_party_id = sorted_scores[2][0]
        party_3_score = sorted_scores[2][1]

        # sends results to 'Test' in db
        test = Test(date=datetime.datetime.now(), answers=answer_string, user_id=last_user_id,
                    party_1_id=first_party_id, party_2_id=second_party_id, party_3_id=third_party_id,
                    party_1_score=party_1_score, party_2_score=party_2_score, party_3_score=party_3_score)
        db.session.add(test)
        db.session.commit()

        return redirect('results')


# displays top 3 matches, corresponding scores, and links to info of the parties
@app.route('/results')
def results():
    first_match_id = Test.query.order_by(Test.date.desc()).first().party_1_id
    second_match_id = Test.query.order_by(Test.date.desc()).first().party_2_id
    third_match_id = Test.query.order_by(Test.date.desc()).first().party_3_id

    first_party = Parties.query.get(first_match_id).name
    first_score = Test.query.order_by(Test.date.desc()).first().party_1_score
    second_party = Parties.query.get(second_match_id).name
    second_score = Test.query.order_by(Test.date.desc()).first().party_2_score
    third_party = Parties.query.get(third_match_id).name
    third_score = Test.query.order_by(Test.date.desc()).first().party_3_score

    # create and display figure (opens in new tab)
    fig = go.Figure(
        data=[go.Bar(x=[first_party, second_party, third_party], y=[first_score, second_score, third_score])],
        layout_title_text="Top Party Matches",
    )
    fig.update_layout(xaxis_title="Party", yaxis_title="Match Index", width=800, height=950)
    fig.show()

    return render_template('results.html', first_party=first_party, first_score=first_score, second_party=second_party,
                           second_score=second_score, third_party=third_party, third_score=third_score)
