#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:shenhaodong
# datetime:2020-08-04 11:19
# software: PyCharm

from  flask import Flask
from config import config

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    # db.init_app(app)
    # #
    # with app.app_context():
    #     db.create_all()


    # @app.route('/')
    # def hello():
    #     return "hello world"

    from application.view.login import login_view
    app.register_blueprint(login_view.bp)
    from application.view.books import view
    app.register_blueprint(view.bp)
    return app