#_*_coding:UTF-8_*_
from Blog import app
from flask import Flask, render_template,session,redirect,url_for,flash


from forms import NameForm
import models


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def formF():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        user = models.User.query.filter_by(username = form.name.data).first()
        if user is None:
            user = models.User(username = form.name.data)
            models.db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
    return render_template('form.html',form = form, known = session.get('known',False))
