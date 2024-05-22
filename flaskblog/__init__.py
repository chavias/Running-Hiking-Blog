from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config


load_dotenv()


# import secrets
# secrets.token_hex

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'user.login'
login_manager.login_message_category = 'info'

mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app

'''
!!! in the terminal !!! 

from flaskblog import db, create_app

app = create_app()
with app.app_context():
    db.create_all()


from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from flaskblog import models

Base = declarative_base()
engine = create_engine('sqlite:///site.db')
Base.metadata.create_all(bind=engine)


from flaskblog import app, db
from flaskblog.models import User, Post # this has to be imported before the database is created
with app.app_context(): 
    app.create_all()
'''

