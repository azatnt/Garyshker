from django.contrib import admin
from django.contrib.admin import AdminSite
from User.models import *
from .models import Dobro



class DobroAdminSite(AdminSite):
    site_header = 'Garyshker Dobro Admin'
    index_title = 'Welcome, Admin'

dobro_admin_site = DobroAdminSite('dobro_admin')

dobro_admin_site.register(Profile)
dobro_admin_site.register(Dobro)
