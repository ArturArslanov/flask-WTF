import os

from flask import app, Flask, url_for, render_template, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    TextAreaField, SelectField, SelectFieldBase
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'really_secret_config_key'

params = {'title': 'захват марса',
          'header': 'Миссия Колонизация Марса!',
          'text': 'И на Марсе будут яблони цвести!',
          'source': 'static/css/style.css'}


class LoginForm(FlaskForm):
    username = StringField('Имя', validators=[DataRequired()],
                           description='обязательный')
    surname = StringField('Фамилия', validators=[DataRequired()],
                          description='обязательный')
    education = StringField('образование', validators=[DataRequired()],
                            description='обязательный')
    sex = SelectField('пол', validators=[DataRequired()],
                      choices=['Мужской', 'Женский'], )
    prof = SelectField('профессия', validators=[DataRequired()],
                       choices=['инженер-исследователь', 'пилот',
                                'строитель',
                                'экзобиолог', 'врач',
                                'инженер по терраформированию', 'климатолог',
                                'специалист по радиационной защите',
                                'астрогеолог', 'гляциолог',
                                'инженер жизнеобеспечения', 'метеоролог',
                                'оператор марсохода',
                                'киберинженер', 'штурман', 'пилот дронов'])
    motive = TextAreaField("мотивация")
    submit = SubmitField('Продолжить')


@app.route('/answer', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    params['source2'] = '../' + params['source']
    if form.validate_on_submit():
        params['username'] = request.form['username']
        params['surname'] = request.form['surname']
        params['education'] = request.form['education']
        params['prof'] = request.form['prof']
        params['sex'] = request.form['sex']
        params['motive'] = request.form['motive'] if request.form[
            'motive'] else 'отсутствует'
        return redirect('/auto_answer')
    return render_template('answer.html', form=form, **params)


@app.route('/auto_answer')
def auto_answer():
    params['source2'] = '../' + params['source']
    # print(request)

    return render_template('answer.html', **params)


@app.route('/')
@app.route('/index')
@app.route('/<string:title>')
@app.route('/index/<string:title>')
def index(title='заголовок не указан'):
    params['title'] = title
    return render_template('base.html', **params)


@app.route('/training/<prof>')
@app.route('/training')
def profession(prof=None):
    if not prof:
        return redirect('/')
    if any(i in prof for i in ('инженер', 'строитель')):
        params['img'] = url_for('static', filename='img/worker.png')
        params[
            'text1'] = f'тренажёры по специальности {prof.replace("строитель", "").replace("инженер", "")}'
    else:
        params['img'] = url_for('static', filename='img/science.png')
        params['text1'] = 'научные стимуляторы'
    print(params['text1'])
    params['source2'] = '../' + params['source']
    return render_template('prof.html', **params)


@app.route('/list_prof/<l>')
def list_prof(l):
    if l == 'ol':
        params['text2'] = 0
    elif l == 'ul':
        params['text2'] = 1
    else:
        params['text2'] = f'НЕВЕРНЫЙ ПАРАМЕТР {l}'
    params['professions'] = ['инженер-исследователь', 'пилот', 'строитель',
                             'экзобиолог', 'врач',
                             'инженер по терраформированию', 'климатолог',
                             'специалист по радиационной защите',
                             'астрогеолог', 'гляциолог',
                             'инженер жизнеобеспечения', 'метеоролог',
                             'оператор марсохода',
                             'киберинженер', 'штурман', 'пилот дронов']
    params['source2'] = '../' + params['source']
    return render_template('list_prof.html', **params)


@app.route('/distribution')
def dist():
    astro = ['Джек Воробей', 'Джеймс', 'Райнер', 'Сара', 'Уильям']
    params['astro'] = astro
    params['source2'] = '../' + params['source']
    return render_template('dist.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
