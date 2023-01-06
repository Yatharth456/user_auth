from flask import Flask
from flask_pymongo import PyMongo
from .auth.auth import bp


def create_app():
    app = Flask(__name__)
    app.secret_key = "secret key"
    app.config['MONGO_URI'] = 'mongodb+srv://goswami2001yatharth:zaqYdXCS7Z1Nx0Sb@cluster0.x2mdlxn.mongodb.net/test'
    app.register_blueprint(bp)
    PyMongo(app)
    return app