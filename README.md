# steptech_assignment
Assignment of Steptech

Instructions
Environment Setup:

Install Python 3.x on your machine.
Install Flask using pip: `pip install django`.
Install MySQL and set up a local database.

Task 1: Flask API Development
a. Create a new Flask/Django application.
Solution: 

        py django-admin startproject stepTech
        cd /stepTech
        py django-admin startapp app
  
b. Define a route `/hello` that returns the string "Hello, World!" when accessed.
Solution:

        urls.py:  path('hello/', views.hello, name='hello'),
        views.py : def hello(request):
                        return render(request, "home.html")
        


      
c. Implement a route `/users` that retrieves a list of users from a MySQL database and display as a
list in html table.
Solution:

        urls.py :  path('users/', views.users, name='users'),
        views.py:  
                  def users(request):
                      all_users = User.objects.all()
                      return render(request, 'users.html', {'users': all_users})


d. Implement a route `/new_user` render html page to accept input from the user and store the
information in database
Solution: 

        urls.py:   path('new_user/', views.new_user, name='new_user'),
        views.py: 
                    def new_user(request):
                        if request.method == 'POST':
                            name = request.POST.get('name')
                            email = request.POST.get('email')
                            role = request.POST.get('role')
                            user = User.objects.create(name=name, email=email, role=role)
                            return redirect('users')
                            # return JsonResponse({'message': 'User created successfully!'})
                        return render(request, 'new_users.html')


e. Create a route `/users/<id>` that retrieves a specific user's details from the database
f. Add error handling to handle cases when a user or resource is not found.
Solution: 

        NOTE: I combined e and f question.
        urls.py:     path('users/<int:id>/', views.user_details, name='user_details'),
        views.py:  
                      def user_details(request, id):
                          user = get_object_or_404(User, id=id)
                          return render(request, 'user_details.html', {'user': user})
      
Note : For beautification you can use bootstrap, tailwind or custom css of any css framework of your
choice, but it is not mandatory, you can skip if you want.
Answer: 
        
        I'm using Tailwind and CSS via CDN.


Task 2: Database Interaction
a. Create a MySQL database with the name "users".
Solution: 

        CREATE DATABASER users;
        
b. Design a table "users" with the following columns:
- id (int, primary key)
- name (varchar)
- email (varchar)
- role (varchar)
  Solution:

                  CREATE TABLE `app_user` (
                  `id` bigint NOT NULL AUTO_INCREMENT,
                  `name` varchar(255) NOT NULL,
                  `email` varchar(255) NOT NULL,
                  `role` varchar(255) NOT NULL,
                  PRIMARY KEY (`id`)
                ) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
  
c. Write SQL queries to:
- Insert sample data into the "users" table.
  Solution: -
  
                INSERT INTO users.app_user (id, name, email, role)
                VALUES
                    (3, 'John Doe', 'john@example.com', 'Admin'),
                    (4, 'Jane Smith', 'jane@example.com', 'User'),
                     (5, 'Bob Johnson', 'bob@example.com', 'User');
    
- Retrieve all users from the "users" table.
  Solution:
  
          select * from users.app_user
  
- Retrieve a specific user by their ID.
  Solution:

       SELECT * FROM users.app_user WHERE id = 1;

  
Task 3: Version Control with Git
a. Initialize a new Git repository for your Django project.
b. Create a branch named "steptech_assignment".
c. Make necessary commits as you implement the Flask API and database functionality.
d. Push your branch to a remote Git repository (GitHub, GitLab, etc.).
e. Create a pull request from your branch to the main branch (or master branch) of the repository.
Solutio: 

        Task 3 every instruction is done.


Task 4: Documentation
a. Write a brief README file that includes instructions on how to set up and run your django
application.
Steps:

        1. Create django project and create django app inside the django project folder.
        2. Create model in inside the app/modle.py.
        3. Connect the MySQL database with django, in setting.py file , which is present in project            folder.
        
                DATABASES = {
                    'default': {
                        'ENGINE': 'django.db.backends.mysql',
                        'NAME': 'your-database-name',
                        'USER': 'your-username',
                        'PASSWORD': 'your-password',
                        'PORT': 'your-port no'
                    }
                }
                
        4. Then give command in termnial: py manage.py makemigrations and py manage.py migrate
        5. Then html template.
        6. Then create function , which do post or get request.
        7. Then run our project using cmd: py manage.py runserver
        
b. Include information about the database schema and how to populate it with sample data.
Solution: 

                Every thing is menstioned on top.
