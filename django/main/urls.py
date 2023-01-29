from django.urls import path
from .views import main_view, home_page_view, list_view

urlpatterns = [
    path("", main_view, name='main'),
    path('home', home_page_view, name='home'),
    path('car', list_view, name='create_car'),
]