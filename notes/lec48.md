# working with django signals
- to make when the user create an account so automatically create a profile we will use `signals` its a way to get notified if a certain action happen in a certain model in the database, rather than do it manually django signal do it for us
- as an example here in the code what we need to do is once the user is created then we want to create a profile, so rather than go to the Profile table and create it manually we use the signals to handle it                                                       
- create signals py make a `signal.py` folder. [check this](../django/users/signals.py)
- after that we have to register this signal so we can use it. How?
    - go to the `__init__.py`  inside the folder which have the `signals.py` in it, add this:
    ```python
    default_app_config = 'app_name.apps.UsersConfig'
    ```
    - then go to `app.py` and add this function:
    ```python
    def ready(self):
        import app_name.signals
    ``` 