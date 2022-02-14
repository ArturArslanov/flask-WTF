from flask import app, Flask, url_for, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'really_secret_config_key'


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


@app.route('/')
@app.route('/index')
def index():
    params = {'title': 'загатовка',
              'header': 'Миссия Колонизация Марса',
              'text': 'И на Марсе будут яблони цвести!',
              'href': f"{url_for('static', filename='css/style.css')}"}
    return render_template('base.html', **params)


@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/succes')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/succes')
def succes_login_up():
    return redirect('/index')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
