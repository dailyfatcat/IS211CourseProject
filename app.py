from flask import Flask
from flask import current_app, g, render_template
from flask.cli import with_appcontext

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    '''Show the login page'''
    return(render_template("login.html"))


if __name__ == '__main__':
    app.run()
