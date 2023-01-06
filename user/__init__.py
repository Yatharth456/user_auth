from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = "secret key"

    from user.registeruser.views import bp
    
    app.register_blueprint(bp, url_prefix= "/")

    return app