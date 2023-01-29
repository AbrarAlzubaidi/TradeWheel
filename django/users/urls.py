from django.urls import path
from .views import login_view, register_view, RegisterView, logout_view

urlpatterns = [
    path("login", login_view, name='login'),
    # path("register", register_view, name='register'),
    path("register", RegisterView.as_view(), name='register'), #to register class based view
    path("logout", logout_view, name='logout'),
]