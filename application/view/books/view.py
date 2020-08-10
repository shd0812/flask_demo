#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:shenhaodong
# datetime:2020-08-09 22:51
# software: PyCharm


from application.model.model import  *

from flask import Blueprint, render_template, redirect, url_for


bp = Blueprint('book', __name__, url_prefix='/book')


@bp.route('/list')
def book_list():

    author = Author.query.all()
    book = Books.query.all()
    for  a in author:
        print(a.books)
    return render_template('books/books.html', author = author)
