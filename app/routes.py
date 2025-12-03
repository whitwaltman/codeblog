from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

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

@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data
        ))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)