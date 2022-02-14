from flask import app, Flask, url_for, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'really_secret_config_key'

params = {'title': 'захват марса',
          'header': 'Миссия Колонизация Марса!',
          'text': 'И на Марсе будут яблони цвести!',
          'source': 'static/css/style.css'}


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


@app.route('/')
@app.route('/index')
@app.route('/<string:title>')
@app.route('/index/<string:title>')
def index(title='заголовок не указан'):
    params['title'] = title
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


@app.route('/training/<prof>')
@app.route('/training')
def profession(prof=None):
    if not prof:
        return redirect('/')
    if any(i in prof for i in ('инженер', 'строитель')):
        params['img'] = url_for('static', filename='img/worker.png')
        profes = prof.split()
        for i in prof:
            if not any(j in i for j in ('инженер', 'строитель')):
                profes = i
            break
        params['text1'] = f'тренажёры по специальности {profes}'
    else:
        params['img'] = url_for('static', filename='img/science.png')
        params['text1'] = 'научные стимуляторы'
    params['source2'] = '../' + params['source']
    return render_template('prof.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
