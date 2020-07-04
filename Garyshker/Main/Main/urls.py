"""Main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from Dobro.admin import dobro_admin_site
from Obrazovanie.admin import report_admin_site, video_admin_site
from Garyshker.admin import super_admin_site




urlpatterns = [
    path('admin/', super_admin_site.urls),
    path('dobro_admin', dobro_admin_site.urls),
    path('report_admin', report_admin_site.urls),
    path('video_admin', video_admin_site.urls),
    path('', include('Garyshker.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
