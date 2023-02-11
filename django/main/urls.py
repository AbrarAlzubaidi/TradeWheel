from django.urls import path
from .views import main_view, home_page_view, list_view, detail, edit_view

urlpatterns = [
    path("", main_view, name='main'),
    path('home', home_page_view, name='home'),
    path('car', list_view, name='create_car'),
    path('car/<str:car_id>/', detail, name='car_details'),
    path('car/<str:car_id>/edit', edit_view, name='edit_car'),
]