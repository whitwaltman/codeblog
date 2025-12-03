from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user
import sqlalchemy as alc
from app import db
from app.models import User

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Whit Waltman'}
    posts = [
        {
            'title': 'some title',
            'body': 'some text',
            'tags': ['hello-world']
        },
        {
            'title': 'some title',
            'body': '''
            some longer text! this can span multiple lines in my file
            but it should appear as an unbroken string when rendered
            ''',
            'tags': ['test']
        },
    ]
    return render_template('index.html', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            alc.select(User).where(User.username == form.username.data)
        )
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sig In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
