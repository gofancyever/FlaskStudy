#_*_coding:UTF-8_*_
from . import main
from flask import Flask, render_template,session,redirect,url_for,flash
from .. import db
from .. import models

from Blog.forms import NameForm
import Blog.models


@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html')

@main.route('/form', methods=['GET', 'POST'])
def formF():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        user = Blog.models.User.query.filter_by(username = form.name.data).first()
        if user is None:
            user = Blog.models.User(username = form.name.data)
            Blog.models.db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
    return render_template('form.html',form = form, known = session.get('known',False))
