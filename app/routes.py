from app import app
from flask import render_template
from app.models import Book, Author
from app.register_form import AddBook
from app import db
from flask import flash, redirect, url_for

@app.route('/')
def index():

    return render_template('index.html')


@app.route('/register')
def index():

    return render_template('register.html')