#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:shenhaodong
# datetime:2020-08-09 18:33
# software: PyCharm



from  flask_login import UserMixin

from application.common import db

class User(db.Model, UserMixin):
    __tablename__ = 'tb_user'

    user_id = db.Column('id', db.Integer, primary_key=True)
    accountNumber = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(51), unique=True)
    name = db.Column(db.String(20), unique=True)



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





class Author(db.Model):
    __tablename__ = 'author'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    books = db.relationship("Books",backref = 'author')

    def __repr__(self):
        return  'Author:%s ' % self.name

class Books(db.Model):

    __tablename__ = 'books'

    id = db.Column(db.Integer,primary_key=True)
    book_name = db.Column(db.String(50))
    author_id = db.Column(db.Integer,db.ForeignKey('author.id'))


    def __repr__(self):
        return "Books:%s %s" % (self.book_name, self.author_id)



