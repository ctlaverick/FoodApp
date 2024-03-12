from django.contrib.auth import views as auth_views
from django.urls import path
from . import views as user_view

urlpatterns = [
    path('', user_view.home, name="home"),
    path('register/', user_view.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
]