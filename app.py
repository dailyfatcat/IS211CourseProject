from flask import Flask
from flask import current_app, g, render_template
from flask import current_app, g
import sqlite3
from flask import Markup
import sqlite3
import click
from flask import Flask, redirect, session, url_for, request, flash
from markupsafe import escape
from flask import current_app, g, render_template
from flask.cli import with_appcontext

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


@app.route('/')
def index():
    '''Index page'''
    db = get_db()
    blog_posts = g.db.execute("SELECT posts.title, posts.pub_date, posts.content, authors.author_name, posts.post_id FROM created "
                               "INNER JOIN posts on created.post_id == posts.post_id "
                               "INNER JOIN authors on created.author_id == authors.author_id "
                              "WHERE published == 1 "
                              "ORDER BY posts.pub_date DESC").fetchall()
    return render_template('index.html', blogs=blog_posts)


@app.route('/dashboard', methods=["POST", "GET"])
def dashboard():
    '''Dashboard Page'''
    if not session.get('username'):
        return (redirect(url_for("login")))
    '''Part III Dashboard: View students and quizzes in the class'''
    db = get_db()
    blog_posts = g.db.execute("SELECT posts.title, posts.pub_date, posts.content, authors.author_name, posts.post_id, posts.published FROM created "
                               "INNER JOIN posts on created.post_id == posts.post_id "
                               "INNER JOIN authors on created.author_id == authors.author_id "
                              "ORDER BY posts.pub_date DESC").fetchall()
    return render_template('dashboard.html', blogs=blog_posts)


@app.route('/edit/<int:postID>')
def edit(postID):
    '''Editing the blog post, get the blog posts'''
    if not session.get('username'):
        return (redirect(url_for("login")))
    db = get_db()
    post = g.db.execute("SELECT posts.title, posts.pub_date, posts.content, authors.author_name, posts.post_id, authors.author_id FROM created "
                               "INNER JOIN posts on created.post_id == posts.post_id "
                               "INNER JOIN authors on created.author_id == authors.author_id WHERE created.post_id = ?", (postID,)).fetchone()
    return render_template('edit.html', post=post)


@app.route('/unpublish/<int:postID>')
def unpublish(postID):
    '''Extra Credit: Unpublish a blog post'''
    if not session.get('username'):
        return (redirect(url_for("login")))
    db = get_db()
    g.db.execute("UPDATE posts SET published = 0 WHERE post_id =?", (postID,))
    g.db.commit()
    return (redirect(url_for("dashboard")))


@app.route('/publish/<int:postID>')
def publish(postID):
    '''Extra Credit:Publish a blog post'''
    if not session.get('username'):
        return (redirect(url_for("login")))
    db = get_db()
    g.db.execute("UPDATE posts SET published = 1 WHERE post_id =?", (postID,))
    g.db.commit()
    return (redirect(url_for("dashboard")))


@app.route('/update', methods=["POST", "Get"])
def updatepost():
    '''Updating the blog post, update the blog posts in database'''
    if not session.get('username'):
        return (redirect(url_for("login")))
    title = request.form.get('title')
    content = request.form.get('content')
    postID = request.form.get('postID')
    author = 1
    db = get_db()
    g.db.execute("UPDATE posts SET title = ?, content = ? WHERE post_id =?", (title, content, postID), )
    g.db.commit()
    return (redirect(url_for("dashboard")))


@app.route('/add', methods=["POST", "Get"])
def add():
    '''Add a new blog post'''
    if not session.get('username'):
        return (redirect(url_for("login")))
    title = request.form.get('title')
    content = request.form.get('content')
    author = 1
    db = get_db()
    postID = g.db.execute("INSERT INTO posts (title, content) VALUES (?,?)", (title, content,)).lastrowid
    g.db.execute("INSERT INTO created (author_id, post_id) VALUES (?,?)", (author, postID, ))
    g.db.commit()
    return (redirect(url_for("dashboard")))


@app.route('/delete/<int:postID>')
def delPost(postID):
    '''Delete a blog post'''
    if not session.get('username'):
        return (redirect(url_for("login")))
    db = get_db()
    g.db.execute("DELETE FROM posts WHERE post_id =?", (postID,))
    g.db.execute("DELETE FROM created WHERE post_id =?", (postID,))
    g.db.commit()
    return (redirect(url_for("dashboard")))


@app.route('/<int:postID>')
def post(postID):
    '''Display a blog post'''
    db = get_db()
    post = g.db.execute("SELECT * FROM posts WHERE post_id =?", (postID,)).fetchone()
    author = g.db.execute("SELECT authors.author_id, authors.author_name FROM created INNER JOIN authors on created.author_id == authors.author_id WHERE post_id =?", (postID,)).fetchone()
    page = Markup('<head><link rel="stylesheet" href="static/styles.css"><meta charset="UTF-8"></head>'+ "<body><h1>" + post[1] + "</h1><p>Created On: " + post[2] + "</p><p>Written By: " + author[1] + "</p><br>" + post[3] + "</body>")
    return render_template('post.html', post=page)


@app.route('/create_blog', methods=['GET', 'POST'])
def create_blog():
    '''Create a blog post'''
    if not session.get('username'):
        return (redirect(url_for("login")))
    return render_template('create_blog.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    '''Show the login page'''
    return(render_template("login.html"))


@app.route('/validate', methods=['POST', 'GET'])
def validate():
    '''Validate the Login'''
    username = request.form['username']
    password = request.form['password']
    if username == "sam" and password == "password":
        session['username'] = username
        return(redirect(url_for("dashboard")))
    else:
        return(redirect(url_for("login")))


if __name__ == '__main__':
    app.run()
