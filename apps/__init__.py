"""
Time : 2020/11/23 9:40 
Author : Lyh
File : __init__.py.py 

"""
from flask import Flask

from extends import db
from settings import Development
from apps.user.views import user_bp


def create_app():
    app = Flask(__name__,template_folder='../templates',static_folder='../static')
    app.config.from_object(Development)

    # 初始化db
    db.init_app(app)

    # 注册蓝图
    app.register_blueprint(user_bp)
    return app
