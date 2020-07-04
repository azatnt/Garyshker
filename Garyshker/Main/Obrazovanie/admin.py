from django.contrib import admin
from .models import *
from django.contrib.admin import AdminSite


class ReportAdminSite(AdminSite):
    site_header = 'Garyshker Statiya Admin'
    index_title = 'Welcome, Admin'

report_admin_site = ReportAdminSite('report_admin')

report_admin_site.register(Genre)

report_admin_site.register(Report)

report_admin_site.register(Comment)



class VideoAdminSite(AdminSite):
    site_header = 'Garyshker Video Admin'
    index_title = 'Welcome, Admin'


video_admin_site = VideoAdminSite('video_admin')

video_admin_site.register(Item)

# video_admin_site.register(Format)

video_admin_site.register(Type)
