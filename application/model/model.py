#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:shenhaodong
# datetime:2020-08-09 18:33
# software: PyCharm



from  flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from application.common import db

# 用户表
class User(db.Model, UserMixin):
    __tablename__ = 'user'

    user_id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(252))
    # name = db.Column(db.String(20), unique=True)


    def is_authenticated(self):
        return True

    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return str(self.user_id)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


    def __repr__(self):
        return '<User %r %r>' % (self.username,self.password)





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



