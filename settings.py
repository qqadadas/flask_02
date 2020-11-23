"""
Time : 2020/11/23 9:44 
Author : Lyh
File : settings.py 

"""


class Config:
    # ENV = 'development'
    DEBUG = False
    # SECRET_KEY = 'DEV'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Development(Config):
    ENV = 'development'
    DEBUG = True
    SECRET_KEY = 'DEV'
    # 数据库+数据库驱动://用户名:密码@主机ip:端口/数据库名
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/flask_02'
