#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:shenhaodong
# datetime:2020-08-04 17:59
# software: PyCharm

from application.form.login_form import LoginForm,RegisterForm
from flask import Blueprint,render_template,request,redirect,url_for,flash
from application.model.model import  *
from flask_login import login_user, logout_user, login_required

from application import  login_manager
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():# 判断表单输入是否符合要求
            username = form.username.data
            password = form.password.data
            query_username = User.query.filter_by(username = username).first()
            if query_username:
                if query_username.check_password(password):
                    login_user(query_username)

                    return redirect(url_for('auth.index'))
                else:
                    flash("密码错误")
            else:
                flash("用户不存在")


        else:
            flash(form.password.errors)
    else:
        redirect(url_for('auth.login'))
    return render_template('account/login.html',form=form)



@bp.route('/regist',methods = ['GET','POST'])
def regist():
    form = RegisterForm() # 初始化 注册表单
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            query_username = User.query.filter_by(username = username).first()
            if query_username:
                flash("该用户已存在")
            else:
                password = form.password.data
                try:
                    new_user = User(username = username)
                    new_user.set_password(password)
                    db.session.add(new_user)
                    db.session.commit()
                    return redirect(url_for('auth.login'))
                except Exception as e:
                    flash("注册失败")
                    print("失败原因是:{}".format(e))
                    db.session.rollback()
        else:
            flash(form.username.errors)
            flash(form.password.errors)
            flash(form.password_confirm.errors)
    return render_template('account/reg.html',form=form)

@bp.route('/index')
@login_required
def index():
    return 'welcome'