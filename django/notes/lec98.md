# serving static files
[whitenoise](https://whitenoise.readthedocs.io/en/latest/)

>With a couple of lines of config WhiteNoise allows your web app to serve its own static files

- then run `python manage.py collectstatic` , why? cause each app has it's own static folder when we move from debug mode to production mode we have to collect those static folders into one static folder to make the deployed service take care with the static.