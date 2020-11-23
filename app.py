from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from apps import create_app
from extends import db
from apps.user.models import User

app = create_app()


manager = Manager(app)

# 命令工具
migrate = Migrate(app=app,db=db)
manager.add_command('db',MigrateCommand)


if __name__ == '__main__':
    manager.run()
