# django forms
django has a build-in form called `AuthenticationForm` and we can get it `from django.contrib.auth.forms import AuthenticationForm`

- so we have to inject this form into our form by define a variable and asign its value to this form then pass it as a context_data inside the view. [for example](../django/users/views.py)

- then we have to add it inside the html [like this](../django/users/templates/views/login.html)

- then we should add `django-crispy-form`

## django-crispy-forms
it is a package to:
- work with django forms
- inject bootstrap styling into our forms
- use feature called filters (some functionality of filter form)

### notes:
- when we add `{% csrf_token %}` then click on inspect in the browser we will se an input tag with type hidden which has a token as a value (hashed token value)
- we should add a decorater to make the user see the home page when he/she logged in. decorater is `login_required`
    - then we should add this 2 lines in settings.py ``