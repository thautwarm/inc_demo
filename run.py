from index import make_page
from profile import profile
from log_sign import login_signin

username = '皮一下'
user_number = '42'
user = dict(username=username, number=user_number, avatar='static/th.jpeg')
logo = 'Eager Player'

import flask

app = flask.Flask(__name__)


@app.route('/index')
@app.route('/')
def index():
    print(make_page(user, logo))
    return str(make_page(user, logo))


@app.route('/login')
@app.route('/signout')
@app.route('/logout')
@app.route('/signin')
def ls():
    return str(make_page(user, logo, login_signin()))


@app.route('/profile')
@app.route('/change_info')
def pf():
    return str(make_page(user, logo, profile(user)))


@app.route('/post_here', methods=['POST'])
def post_here():
    return str(flask.request.form)


app.debug = True
app.run(port=5050)
