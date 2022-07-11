from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


db=SQLAlchemy()
DB_Name='Database.db'

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']='My Secret'
    app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{DB_Name}'
    db.init_app(app)

    from .view import view

    app.register_blueprint(view,url_prefix='/')

    # from .models import 
    create_database(app)
    
    # login_manager=LoginManager()
    # login_manager.login_view='auth.homepage'
    # login_manager.init_app(app)

    # @login_manager.user_loader
    # def load_user(id):
    #     return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/'+DB_Name):
        db.create_all(app=app)
        print('Created Database!')