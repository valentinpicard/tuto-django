# tuto-django
Tutorial project for Django

https://www.youtube.com/watch?v=n-FTlQ7Djqc&list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc&ab_channel=NetNinja

## Start with django

- Go inside your work directory 
    - `cd tuto-django`

- Create your django application
    - python3 manage.py startapp "app_name"

- Link with your django project
    - Go in you django settings.py file 
    - Add your app name in the INSTALLED_APPS section

- Add in your app a urls.py file to place urls routes and connect then to our views

- See tuto.urls.py to include the routes

- Run the server
    - python3 manage.py runserver 
    - shortcut : make run

- When you change your db models, you've to do migrations 
	- python3 manage.py makemigrations 
    - python3 manage.py migrate
    - shortcut : make migrate

- Create super user :
    - python3 manage.py createsuperuser
    - for this tuto :
        - user : usertest
        - pwd : test1234

## Notes

The application is separate in two parts :
- tuto which belongs to the django settings
- myapp which is the application
