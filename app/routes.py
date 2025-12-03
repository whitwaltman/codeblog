from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

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
        },
        {
            'title': 'Bulk undo with git',
            'body': '''
            Discard local changes in git (i.e. revert any modifications made to files in your working directory back to their state from your most recent commit):
            <code>git restore file_name</code>. I just did <code>git restore app/__init__.py</code>. If you have a lot of stuff to undo, use <code>git restore .</code>, but beware that it discards all changes that git is tracking (both staged and unstaged!)
            If you want to discard staged changes (i.e. unstage them), use <code>git reset HEAD</code>
            ''',
            'tags': ['git']
        }
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