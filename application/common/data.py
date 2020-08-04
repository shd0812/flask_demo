#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:shenhaodong
# datetime:2020-07-26 15:50
# software: PyCharm


from sqlalchemy import create_engine
from sqlalchemy.sql import text
from config import config

def db_query(sql, config_name,settings=None, echo=None):
    if settings is None:
        settings = config[config_name].SQLALCHEMY_DATABASE_URI

    if echo is None:
        echo = config[config_name].SQLALCHEMY_ECHO

    return create_engine(settings, echo=echo).connect().execute(text(sql).fetchall())


def db_execute(sql, config_name,settings=None, echo=None):
    if settings is None:
        settings = config[config_name].SQLALCHEMY_DATABASE_URI

    if echo is None:
        echo = config[config_name].SQLALCHEMY_ECHO

    return create_engine(settings, echo=echo).connect().execute(text(sql)).rowcount