#!flask/bin/python
import os
from Blog import create_app,db
from Blog.models import User,Role
from flask_script import Manager,Shell
from flask_migrate import Migrate,MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manage = Manager(app)
migate = Migrate(app,db)

def make_shell_context():
    return dict(app = app, db = db, User = User,Role = Role)
manage.add_command('shell',Shell(make_context=make_shell_context))
manage.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manage.run()

7.5