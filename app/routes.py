from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Whit Waltman'}
    return render_template('index.html', title='codeblog', user=user)