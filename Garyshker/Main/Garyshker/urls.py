from django.urls import path
from Garyshker.views import *
from django.contrib.auth import views as auth_view
from User import views as v
from User.views import *
from Dobro.views import *
from Obrazovanie.views import *





urlpatterns = [
    path('', index, name='index_urls'),
    path('register/', v.register, name='register_url'),
    path('login/', auth_view.LoginView.as_view(template_name='user/login.html'), name='login_url'),
    path('logout/', auth_view.LogoutView.as_view(template_name='user/logout.html'), name='logout_url'),
    path('profile/', profiles, name='profile_url'),
    path('charity/', charity, name='charity_url'),
    path('obrazovanie/', show_item, name='obrazovanie_url'),
    path('obrazovanie/reports/', all_reports, name='all_reports_url'),
    path('obrazovanie/reports/<str:slug>', genre_detail_report, name='genre_detail_reports_url'),
    path('obrazovanie/<str:slug>/', genre_detail, name='genre_detail_url'),
    # path('obrazovanie/<int:id>', item_detail, name='item_detail_url'),
    path('obrazovanie/report_detail/<int:id>', report_detail, name='report_detail_url'),
    path('likes/', like_report, name='likes_url'),
    path('search/', SearchField.as_view(), name='search_url'),
    path('search-report/', SearchFieldReport.as_view(), name='search_report_url'),
    path('report/create/', report_create, name='report_create_url'),
    path('report_creation/', after_writing_post, name='after_writing_post_url'),
    path('comment_delete/<int:id>', comment_delete, name='comment_delete_url'),
    path('favourite_reports/<int:id>', favourite_report, name='favourite_post_url'),
    path('favourite_reports', favourite_report_list, name='favourite_report_list_url')



    # path('charity/feedback/', )
]
