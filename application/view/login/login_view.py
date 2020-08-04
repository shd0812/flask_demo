#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:shenhaodong
# datetime:2020-08-04 17:59
# software: PyCharm

from application.form.login_form import LoginForm
from flask import Blueprint,render_template

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    return render_template('login.html',form=form)
