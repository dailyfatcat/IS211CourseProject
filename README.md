<h1><strong>Project Option 2: Blog Application </strong></h1>

<h2>Database</h2> The database has three tables, there is a table for the blog posts and a table for authors. 
Since many authors can make many blog posts the data is normalized and there is a third table containing the post id and author ids, this third table normalizes the data by removing repetitive lines.
The db.py file is used to create the database where the schema is defined in schema.sql. The key is automatically created and auto-incremented.

<h3>Creating the database</h3>
createdb.py creates the initial database and adds two example entries outside of the application. The database is called "blogs.db"

<h2> The Blog Application</h2>
The blog application requires that user logs in, using the session to keep track that the user has logged in to edit the blog posts, delete the blog posts or create new blog posts.
<h3>Login Information</h3>
<strong>username:</strong> sam
<strong>password:</strong> password
Since the project is created for a single user, there is no tracking of multiple users, usernames, or passwords but rather that the user has logged in with the username ‘sam and the password ‘password’.
<h3>Blog Application</h3>
The index page, or main page, queries the database and lists all the posts that a user can view, the user can view the posts here from the links. 
Once the user is logged in, the dashboard page ensures the user is logged in before querying the database to get all the blog posts then render the dashboard template. This is where the user can then choose to edit, delete, or view current blog posts or create a new blog post. The button is clicked to complete the actions. </br>
Every blog post has an auto-incremented key id that is used to find the blog post with a query for editing and deleting. 
