
from flask import app, Flask, url_for,render_template


@app.route('/')
@app.route('/index')
def index():
    user = 'Артур'
    return render_template('index.html',title='первая страница',user_name=user)
