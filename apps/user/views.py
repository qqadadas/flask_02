"""
Time : 2020/11/23 9:48 
Author : Lyh
File : views.py 

"""
from flask import Blueprint, url_for, request, flash, redirect, render_template, g, session

from apps.user.models import User
from extends import db

user_bp = Blueprint('user', __name__)

users = [
]


@user_bp.route('/')
def index():
    # url_for('register')  # 不能直接写，必须要写蓝图下的具体方法
    url_for('user.register')
    return render_template('base.html', users=users)


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        # users.append(
        #     {'username': username, 'password': password}
        # )

        # 1使用模型类并创建对象
        user = User()
        # 2 给对象赋值
        user.username = username
        user.password = password
        # 3添加数据
        db.session.add(user)
        # 4 提交
        db.session.commit()

        return "注册成功"

        # return redirect(url_for('user.index'))

    return render_template('user/register.html')


@user_bp.route('/login', methods=('GET', 'POST'))
def login():
    # print(222)
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        for user in users:
            if user.get('username'):
                # g.user = {'username': username, 'password': password}
                session['username'] = user['username']
                # print(g.user)
                return render_template('user/index.html')
        else:
            return "用户不存在"

    return render_template('user/login.html')


@user_bp.route('/delete',methods=['GET','POST'] )
def delete():
    msg = ''
    if request.method == "POST":
        username = request.form.get("username")
        for user in users:
            if username in user.get('username'):
                users.remove(user)
                return redirect(url_for('user.index'))
        else:
            msg= '用户不存在'

    # flash('用户不存在')
    return render_template('user/delete.html', msg=msg)


@user_bp.route('/update',methods=['GET','POST'] )
def update():
    username = session['username']
    print(username)
    if request.method == "POST":
        newname =request.form.get("username")
        for user in users:
            if username == user.get('username'):
                user['username'] = newname
                return redirect(url_for('user.index'))
        else:
            return '用户不存在'
    else:
        if username:
            return render_template('user/update.html', user=username)
        else:
            return "用户不存在"


@user_bp.route("/logout")
def logout():

    return "再见"
