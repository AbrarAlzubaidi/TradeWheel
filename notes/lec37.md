# introduction of django apps
- migrations folder is a folder that will transfer from python code into SQL code that the ORM (object relationnal mapping) will convert it into SQL queries
- this folder will be updated when we run `python manage.py makemigrations` command
- `__init__.py` file to make the app runs as a module not a script
- `admin.py` file add the functionality for the app to add it into admin panel
- `apps.py` file have the information and details for the app
- `models.py` file to add our app models here and its represent the Entity in SQL
- `tests.py` file to test our app
- `views.py` file to add some functionality to allow us what's going to happen when some user request our app. (endpoints)  