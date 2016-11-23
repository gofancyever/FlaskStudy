from flask_script import Manager, Shell
import models
from Blog import app,manager
from flask_migrate import Migrate, MigrateCommand
def make_shell_context():
    return dict(app=app, db=models.db, User=models.User, Role=models.Role)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)