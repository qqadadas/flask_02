"""
Time : 2020/11/23 14:00 
Author : Lyh
File : models.py 

"""
from extends import db


class User(db.Model):
    id = db.Column(db.INTEGER,primary_key=True,autoincrement=True)
    username =db.Column(db.String(20),nullable=False,unique=False)
    password = db.Column(db.String(8),unique=True)
    phone = db.Column(db.String(11),unique=True)

    def __str__(self):
        return self.username


class Blog(db.Model):
    id = db.Column(db.INTEGER,primary_key=True,autoincrement=True)
    title =db.Column(db.String(200),nullable=False,unique=False)
    content = db.Column(db.String(1000),unique=True)
    # phone = db.Column(db.String(11),unique=True)

    def __str__(self):
        return self.title