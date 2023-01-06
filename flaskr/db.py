from flask_pymongo import PyMongo
from flask import current_app

def get_db():
    return PyMongo(current_app)

