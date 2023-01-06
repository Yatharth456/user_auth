from flask import Blueprint, render_template, request
from user.db import start_db

bp = Blueprint('views', __name__)

@bp.route("/register", methods=('GET', 'POST'))
def register_user():
    user = request.json
    mongo = start_db()

    register = mongo.db.register.insert_one(
        {
        "email": user.get('email'),
        "password": user.get('password'),
        }
    )

    return ({"data": str(register)})
    # return render_template("hello.html")
