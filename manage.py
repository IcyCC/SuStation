# -*- coding:utf-8 -*-  
import os
from app.defin import create_app,db
from app.models import *
from flask.ext.script import Manager,Shell
from flask.ext.migrate import Migrate,MigrateCommand

app = create_app('development')
manager = Manager(app)
migrate = Migrate(app,db)

def make_shell_context():
    return dict(app = app,db = db)

manager.add_command("shell",Shell(make_context=make_shell_context,use_ipython=False))
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()