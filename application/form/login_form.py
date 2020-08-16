#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:shenhaodong
# datetime:2020-08-04 17:37
# software: PyCharm
from flask_wtf import FlaskForm,Form
from wtforms import (
    StringField, PasswordField, BooleanField, SubmitField
)

from wtforms.validators import DataRequired, Length,EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username',render_kw={'placeholder': "your name"}, validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(message=u'密码不能为空'),Length(6,128)])
    # remember = BooleanField('Remember me')
    submit = SubmitField('登录')

class RegisterForm(Form):
    username = StringField('Username',render_kw={'placeholder': "your name"}, validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(message=u'密码不能为空'),Length(6,128)])
    password_confirm = PasswordField('Repeat Password',
                                         validators=[DataRequired(),
                                                     EqualTo('password', message='Passwords must match'), ],
                                         render_kw={"placeholder": "confirm New Password confirmed！"})    # remember = BooleanField('Remember me')
    submit = SubmitField('注册')