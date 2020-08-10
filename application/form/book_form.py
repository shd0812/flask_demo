#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:shenhaodong
# datetime:2020-08-09 23:48
# software: PyCharm


from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, BooleanField, SubmitField
)
from wtforms.validators import DataRequired, Length


class BookForm(FlaskForm):
    # username = StringField('Username',render_kw={'placeholder': "your name"}, validators=[DataRequired()])

    author = StringField("Author", render_kw={'placeholder':'作者名字'}, validators=[DataRequired()])