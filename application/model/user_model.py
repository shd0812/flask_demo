#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:shenhaodong
# datetime:2020-07-26 16:10
# software: PyCharm

from  flask_login import UserMixin

from application.common import db

class User(db.Model, UserMixin):
    user_id = db.Column('id', db.Integer, primary_key=True)
    accountNumber = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(20), unique=True)

    __tablename__ = 'tb_user'

    def __init__(self,user_id = None,
                 account_num=None,
                 password=None,
                 name='anonymous'):
        self.user_id = user_id
        self.accountNumber = account_num
        self.password = password
        self.name = name

    def is_authenticated(self):
        return True

    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return str(self.user_id)

    def __repr__(self):
        return '<User %r %r>' % (self.accountNumber,self.password)