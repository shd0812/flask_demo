#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:shenhaodong
# datetime:2020-07-26 15:28
# software: PyCharm

from flask import Flask
from flask_login import LoginManager
from application.common import db

login_manager = LoginManager()
login_manager.login_view = "user.login"
