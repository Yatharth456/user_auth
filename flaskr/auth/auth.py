from flask import Blueprint, request
from flaskr.db import get_db
import hashlib

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    try:
        user = request.json
        mongo = get_db()
        new_register = mongo.db.register.insert_one(
            {
                "email": user.get('email'),
                "password": hashlib.sha256("a".encode('utf-8')).hexdigest(),
            }
        )
        return ({"message": str(new_register)})
    except Exception as e:
        return {
            "message": "Something went wrong",
            "error": str(e),
            "data": None
        }, 500
