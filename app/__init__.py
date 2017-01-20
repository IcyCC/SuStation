from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_pagedown import PageDown
from config import config
from config import config
from flask_pagedown import  PageDown

bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()
pagedown = PageDown()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)


    bootstrap.init_app(app)
    moment.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    pagedown.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    #from .auth import auth as auth_blueprint
    #app.register_blueprint(auth_blueprint)

    from .write import write as write_blueprint
    app.register_blueprint(write_blueprint,url_prefix = '/write')

    return app