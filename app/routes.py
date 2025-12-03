from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Whit Waltman'}
    posts = [
        {
            'title': 'Abstracting out operations w/ arrow functions',
            'body': '<code>const randItems = arr => arr[Math.floor(Math.random() * arr.length)];</code>',
            'tags': ['javascript']
        },
        {
            'title': 'Get directories that start with a lowercase letter',
            'body': '''
            Most computers come with a few default directories created, e.g. Documents, Library, Music, etc. I like to use lowercase
            letters for the folders I create, like dotfiles or utils. If I want to list them and filter out any folders starting with a capital letter, I can use grep.
            <code>ls -1 | grep "^[a-z]"</code> works, but so does <code>ls -1 | grep -v "[A-Z]"</code>, as long as your lowercase directories don't have any uppercase letters in their name at all.
            ''',
            'tags': ['grep', 'regex', 'filesystem']
        },
        {
            'title': 'Running a flask app',
            'body': '''
            I try to always name my virtual environments "venv", although that can be confusing for some. I just run
            <code>source venv/bin/activate</code> to enter my virtual environment, and then do <code>flask run</code>. This works because I have a file in the root of my project called ".flaskenv"
            which contains the line "FLASK_APP=name_of_my_app.py". Alternatively, I could name my main python file "app.py" or "wsgi.py", or use the command "flask --app name_of_my_app run" to tell Flask
            what the name of my app is.
            ''',
            'tags': ['flask']
        }
    ]
    return render_template('index.html', title='codeblog', user=user, posts=posts)