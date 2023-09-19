# tuto-django
Tutorial project for Django

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