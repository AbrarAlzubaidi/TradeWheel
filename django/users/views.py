from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from main.views import home_page_view

def login_view(request):
    """
    login view has 2 requests, one is the get method and when it happens:
            then we will render the form
        the second one when the post request happens
            then we will pass the data 
    """
    if request.method == 'POST':
        login_form = AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print('the authinticated user is: ', user)
            if user is not None:
                login(request, user)
                return redirect(home_page_view)
            else:
                pass
    elif request.method == 'GET':
        login_form = AuthenticationForm
    return render(request, 'views/login.html', {'login_form': login_form})