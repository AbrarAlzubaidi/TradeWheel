from django.shortcuts import render
from django.http import HttpResponse

# create a view that responsible to show themain page that will appear when any user will navigate to the website

def main_view(request):
    """
    landing page when user navigates into the website
    that will return a http response
    """
    template_path = "main/main.html"
    return render(request, template_path, {"name": "automax"})
    # {"name": "automax"} this dictionary is for pass avalue to the template

def home_page_view(request):
    """
    home page view when user logged in
    """
    print(request.user.username)
    return render(request, "main/home.html")