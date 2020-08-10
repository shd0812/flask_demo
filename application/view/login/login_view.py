#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:shenhaodong
# datetime:2020-08-04 17:59
# software: PyCharm

from application.form.login_form import LoginForm
from flask import Blueprint,render_template,request,redirect,url_for,flash


bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            print(form.username.data)

            return redirect(url_for('auth.index'))
        else:
            flash(form.password.errors)
    else:
        flash("我是get")
    return render_template('account/login.html',form=form)


@bp.route('/index')
def index():
    return 'welcome'