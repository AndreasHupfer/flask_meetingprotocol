from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Andreas Hupfer'}
    protocols = [
        {
            'subject': 'VS Sitzung 22.01.2021',
            'Date': '22.01.2021',
            'owner': {'username': 'Andreas Hupfer'}
        },
        {
            'subject': 'VS Sitzung 24.02.2021',
            'Date': '24.02.2021',
            'owner': {'username': 'Andreas Hupfer'}
        }
    ]
    return render_template('index.html', title='Home', user=user, protocols=protocols)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requestet for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', titel='Sign in', form=form)
