<h1><strong>Project Option 2: Blog Application </strong></h1>

<h2>Database</h2> The database has three tables, there is a table for the blog posts and a table for authors. 
Since many authors can make many blog posts the data is normalized and there is a third table containing the post id and author ids, this third table normalizes the data by removing repetitive lines.
To complete the extra credit, there is an integer called "published" by default the blog entry is published.
If the user does not want to publish the blog, they can click the unpublish button to change the status.


<h3>Creating the database</h3>
The createdb.py file was used to create the database from the schema that is defined in schema.sql. The primary key is automatically created and auto-incremented.
createdb.py also adds two example entries outside of the application. The database for the application is called "blogs.db".

<h2> The Blog Application</h2>
The blog application requires that user logs in, using the session to keep track that the user has logged in to edit the blog posts, delete the blog posts or create new blog posts.
<h3>Login Information</h3>
<strong>username:</strong> sam </br>
<strong>password:</strong> password </br>
Since the project is created for a single user, there is no tracking of multiple users, usernames, or passwords but rather that the user has logged in with the username ‘sam' and the password ‘password’.
<h3>Blog Application</h3>
The index page, queries the database and lists all the posts that a user can view, the user can view the posts here from the links.
The links use an app route that uses the post ID to display the posts content. 
Every blog post has an auto-incremented key id that is used to find the blog post with a query for editing and deleting.</br>
Once the user is logged in, the dashboard page ensures the user is logged in before querying the database to get all 
the blog posts then render the dashboard template. 
This is where the user can then choose to edit, delete, or view current blog posts or create a new blog post. 
The button is clicked to complete the action required. </br>
The edit/postID is used to query the database to get the blogs current content so the logged in user can edit the title and post content.
This calls the update route which updates the posts content and title. 
The error handling is handled in the HTML, the user is required to enter some content, the fields cannot be left blank. </br>
The add route and create_blog allows for the new blog posts to be added to the database, updating the posts and created tables in the database. Retrieves the content from the HTML form, where the error handling is also considered ensuring the user must enter some text.</br>
The delPost route search the database for the post that the user has clicked the button for. </br>
The route postid, queries the database to get the information needed to display the blog post</br>
<h4>Extra Credit:</h4>
<strong>PermaLinks</strong> Each blog post has its own link, which can be clicked on to view the blog posts. </br>
<strong>Publish</strong> Two routes were created, publish and unpublished so the user can decide to publish or unpublish the posts. This updates the published value in the database. 
A Status is displayed so the user can tell if there post if published or not </br>



