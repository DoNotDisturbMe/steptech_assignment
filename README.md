# steptech_assignment
Assignment of Steptech

Instructions
Environment Setup:

Install Python 3.x on your machine.
Install Flask using pip: `pip install django`.
Install MySQL and set up a local database.

Task 1: Flask API Development
a. Create a new Flask/Django application.
b. Define a route `/hello` that returns the string "Hello, World!" when accessed.
c. Implement a route `/users` that retrieves a list of users from a MySQL database and display as a
list in html table.
d. Implement a route `/new_user` render html page to accept input from the user and store the
information in database
e. Create a route `/users/<id>` that retrieves a specific user's details from the database
f. Add error handling to handle cases when a user or resource is not found.
Note : For beautification you can use bootstrap, tailwind or custom css of any css framework of your
choice, but it is not mandatory, you can skip if you want.


Task 2: Database Interaction
a. Create a MySQL database with the name "users".
b. Design a table "users" with the following columns:
- id (int, primary key)
- name (varchar)
- email (varchar)
- role (varchar)
c. Write SQL queries to:
- Insert sample data into the "users" table.
- Retrieve all users from the "users" table.
- Retrieve a specific user by their ID.

  
Task 3: Version Control with Git
a. Initialize a new Git repository for your Flask/Django project.
b. Create a branch named "steptech_assignment".
c. Make necessary commits as you implement the Flask API and database functionality.
d. Push your branch to a remote Git repository (GitHub, GitLab, etc.).
e. Create a pull request from your branch to the main branch (or master branch) of the repository.


Task 4: Documentation
a. Write a brief README file that includes instructions on how to set up and run your Flask
application.
b. Include information about the database schema and how to populate it with sample data.
