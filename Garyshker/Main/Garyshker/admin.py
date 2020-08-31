from django.contrib import admin
from Obrazovanie.models import *
from Dobro.models import *
from User.models import *
from django.contrib.admin import AdminSite


class MainAdmin(AdminSite):
    site_header = 'Super Admin'
    index_title = 'Welcome, Super Admin'
    password = 'Admin12345'

super_admin_site = MainAdmin('super_admin')


super_admin_site.register(Genre)
super_admin_site.register(Report)
super_admin_site.register(Comment)
super_admin_site.register(Item)
super_admin_site.register(Format)
super_admin_site.register(Type)
super_admin_site.register(Profile)
super_admin_site.register(User)



#
#
#
# admin.site.register(Genre)
# admin.site.register(Report)
# admin.site.register(Comment)
# admin.site.register(Item)
# admin.site.register(Format)
# admin.site.register(Type)
# admin.site.register(Profile)
