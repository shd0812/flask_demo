#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:shenhaodong
# datetime:2020-08-04 17:37
# software: PyCharm
from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, BooleanField, SubmitField
)

from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username',render_kw={'placeholder': "your name"}, validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(message=u'密码不能为空'),Length(8,128)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')

