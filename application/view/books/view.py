#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:shenhaodong
# datetime:2020-08-09 22:51
# software: PyCharm


from application.model.model import  *

from flask import Blueprint, render_template, redirect, url_for,flash,request
from application.form.book_form import BookForm

bp = Blueprint('book', __name__, url_prefix='/book')


@bp.route('/delete_book/<book_id>')
def delete_book(book_id):
    book = Books.query.get(book_id)
    if book:
        try:
            db.session.delete(book)
            db.session.commit()
        except Exception as e:
            flash(e)
            db.session.rollback()
    else:
        flash("书籍不存在")
    return redirect(url_for("book.book_list"))




@bp.route('/list',methods=['GET','POST'])
def book_list():

    # 自定义bookform表单
    book_form = BookForm()

    # 调用wtf验证
    if book_form.validate_on_submit():
        author = book_form.author.data # 获取作者
        book = book_form.book.data  #获取书籍
        author_parm = Author.query.filter_by(name = author).first() #查询数据库是否有该作者
        print(author_parm)
        if author_parm: # 如果作者存在
            book_name = Books.query.filter_by(book_name = book).first()
            if book_name:  # 如果存在
                flash("有重复书籍")
            else:  # 不存在
                try:
                    new_book = Books(book_name=book,author_id= author_parm.id)
                    db.session.add(new_book)
                    db.session.commit()
                except Exception as e:
                    flash("添加书籍失败")
                    print(e)
                    db.session.rollback()
        else: # 作者不存在
            try:
                new_author = Author(name=author)
                db.session.add(new_author)
                db.session.commit()
                book_result =Books.query.filter_by(book_name = book).first()
                if book_result: # 如果存在
                    flash("有重复书籍")
                else: #不存在
                    try:
                        new_book = Books(book_name=book,author_id=new_author.id)
                        db.session.add(new_book)
                        db.session.commit()
                    except Exception as e:
                        flash("添加书籍失败")
                        print(e)
                        db.session.rollback()

            except Exception as e:
                flash(e)
                #回滚
                db.session.rollback()
    else:
        if request.method =='POST':
            print("23123123")
            flash("参数不全")
    author = Author.query.all()
    book = Books.query.all()
    for  a in author:
        print(a.books)
    return render_template('books/books.html', author = author, form = book_form)
