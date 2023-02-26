# Gunicorn production server
[gunicorn](https://gunicorn.org/)
Gunicorn is a pure-Python HTTP server for WSGI applications. It allows you to run any Python application concurrently by running multiple Python processes within a single dyno

rather than run the server by `python maage.py runserver` we can run our app by `python -m gunicorn <project_name>.wsgi`

## What is Gunicorn vs nginx?
Gunicorn implements the Web Server Gateway Interface (WSGI), which is a standard interface between web server software and web applications. Nginx is a web server. It's the public handler, more formally called the reverse proxy, for incoming requests and scales to thousands of simultaneous connections