import sqlite3

connection = sqlite3.connect('blogs.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

db = connection.cursor()

db.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
           ('Example Post', 'Here is an Example')
           )
db.execute("INSERT INTO authors (author_name) VALUES (?)", ("Sam",))
db.execute("INSERT INTO created (author_id, post_id) VALUES (?, ?)", (1, 1))

connection.commit()
connection.close()