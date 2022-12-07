from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from main.views import home_page_view
from django.contrib import messages

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
                messages.success(request, 'logged in successfully')
                return redirect(home_page_view)
            else:
                # if the user not saved in the database then the user should create 
                # a new account (register)
                # then redirect him/her into login page
                messages.error(request, 'unfortunatly we cant see ur name with us try to register')
        else:
          messages.error(request, 'unfortunatly we cant see u with us')  
    elif request.method == 'GET':
        login_form = AuthenticationForm
    return render(request, 'views/login.html', {'login_form': login_form})