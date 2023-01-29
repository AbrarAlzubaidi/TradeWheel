# loading static assets django
1. static folder live inside the app level 
2. whenever we change something in the templates we have to shutdown the server and re-run it again
3. `<link href="{% static 'css/bootstrap.min.css' %}" rel="stylesheet">`
4. `{% load static %}` in the first of the html