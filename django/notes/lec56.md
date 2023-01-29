# deals with django messages
[docs](https://docs.djangoproject.com/en/4.1/ref/contrib/messages/)

- first we have to include at which template we need to show the message?, here for example we will show it in `base.html` by doing this script
```python
{% if messages %}
    {% for message in messages %}
        {{message}}
    {% endfor %}
{% endif %}
```
- then we will assign a success message when the user logged in by doing this inside login_view function:
```python
messages.success(request, 'logged in successfully')
```
- then go to the settings.py (to define our custom tags)
```python
from django.contrib.messages import constants as messages
MESSAGES_TAGS = {
    messages.ERROR: 'danger'
}
```