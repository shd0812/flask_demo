#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:shenhaodong
# datetime:2020-07-26 15:26
# software: PyCharm


from flask_sqlalchemy import SQLAlchemy

__all__ = ("db")

db = SQLAlchemy()