from markupsafe import escape
from flask import *
from flask_pymongo import PyMongo

app = Flask(__name__)
app.secret_key = "secret key"
app.config['MONGO_URI'] = 'mongodb+srv://goswami2001yatharth:zaqYdXCS7Z1Nx0Sb@cluster0.x2mdlxn.mongodb.net/test'
mongo = PyMongo(app)

@app.route('/')
@app.route('/index/')
def hello():
    return '<h1>Hello, World!</h1>'


@app.route('/about/')
def about():
    return '<h3>This is a Flask web application.</h3>'

@app.route('/capitalize/<word>/')
def capitalize(word):
    return '<h1>{}</h1>'.format(escape(word.capitalize()))

@app.route('/add/<int:n1>/<int:n2>/')
def add(n1, n2):
    return '<h1>{}</h1>'.format(n1 + n2)

@app.route('/users/<int:user_id>/')
def greet_user(user_id):
    users = ['Bob', 'Jane', 'Adam']
    try:
        return '<h2>Hi {}</h2>'.format(users[user_id])
    except IndexError:
        abort(404)
 

    
@app.route('/cookie')  
def cookie():  
    res = make_response("<h1>cookie is set</h1>")  
    res.set_cookie('foo','bar')  
    return res  
  
if __name__ == '__main__':  
    app.run(debug = True)