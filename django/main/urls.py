from django.urls import path
from .views import main_view, home_page_view

urlpatterns = [
    path("", main_view, name='main'),
    path('home', home_page_view, name='home')
]