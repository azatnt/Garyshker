from django.urls import path
from Garyshker.views import *
from django.contrib.auth import views as auth_view
from User import views as v
from User.views import *
from Dobro.views import *





urlpatterns = [
    path('', index, name='index_urls'),
    path('register/', v.register, name='register_url'),
    path('login/', auth_view.LoginView.as_view(template_name='user/login.html'), name='login_url'),
    path('logout/', auth_view.LogoutView.as_view(template_name='user/logout.html'), name='logout_url'),
    path('profile/', profiles, name='profile_url'),
    path('charity/', charity, name='charity_url'),
]