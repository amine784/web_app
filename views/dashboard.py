from flask import render_template, Blueprint

dash = Blueprint('dashboard', __name__,url_prefix='/dash')


@dash.route('/')
def dashb():
    return(render_template('admin.html'))

@dash.route('/user')
def user():
    return(render_template('user.html'))