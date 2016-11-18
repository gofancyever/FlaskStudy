
from Blog import app
from flask import Flask, render_template,session,redirect,url_for,flash

from flask_bootstrap import Bootstrap
from forms import NameForm


bootstrap = Bootstrap(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def formF():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not  None and old_name != form.name.data:
            flash('Looks like you have change you name!')
        session['name'] = form.name.data
        return redirect(url_for('formF'))
    return render_template('form.html', form=form, name=session.get('name'))