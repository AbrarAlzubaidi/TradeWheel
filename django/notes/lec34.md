# django project structure
- __init__.py -> to make to app executed as a module

- asgi.py file -> standsfor async server gate interface which allowes an external servers/applications interact with django server

- wsgi.py file -> stands for Web Server Gateway Interface which basiclly it is simillar to asgi also we use it when we want to deploy our django app but what is basicly does is it is as an entry point for webserver/applications thar react as webservers to react with the django application 

- settings.py file -> contains all the major settiengs for django project, for ex: secret key, database, installed app
    - if DEBUG inside setting is turned into False then u should add the servers that u want to make it deals with django in the ALLOWED_HOSTS setting then if we refresh the page the 404 page will appear and also what will happen is the CSS going to crash so it will be a normal HTML without any CSS

- `ROOT_URLCONF = 'first_project.urls'`
inside the settigs.py means will execute the main urls file (project level) 