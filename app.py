from flask import Flask
from flask import current_app, g, render_template
from flask import current_app, g
import sqlite3

app = Flask(__name__)
app.secret_key = 'supersecretkey'
DATABASE = 'blogs.db'

def get_db():
    """Connect to the application's configured database. The connection
    is unique for each request and will be reused if this is called
    again.
    """
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row

    return g.db


@app.route('/dashboard', methods=["POST", "GET"])
def dashboard():
    '''Part III Dashboard: View students and quizzes in the class'''
    db = get_db()
    blog_posts = g.db.execute("SELECT posts.title, posts.pub_date, posts.content, authors.author_name, posts.post_id FROM created "
                               "INNER JOIN posts on created.post_id == posts.post_id "
                               "INNER JOIN authors on created.author_id == authors.author_id ").fetchall()
    return render_template('dashboard.html', blogs=blog_posts)


@app.route('/edit', methods=["POST", "GET"])
def edit():
    pass

@app.route('/delete', methods=["POST", "GET"])
def delete():
    pass

@app.route('/login', methods=['GET', 'POST'])
def login():
    '''Show the login page'''
    return(render_template("login.html"))


if __name__ == '__main__':
    app.run()
