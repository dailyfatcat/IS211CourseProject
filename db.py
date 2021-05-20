import sqlite3
from flask import current_app, g

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


def close_db(e=None):
    """If this request connected to the database, close the
    connection.
    """
    db = g.pop("db", None)

    if db is not None:
        db.close()


def init_db():
    """Clear existing data and create new tables."""
    db = get_db()

    with current_app.open_resource('schema.sql', mode='r') as f:
        db.executescript(f.read())

    db.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Example Post', 'Here is an Example')
            )
    db.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
                ('Another Example Post', 'Content for the second post'))


