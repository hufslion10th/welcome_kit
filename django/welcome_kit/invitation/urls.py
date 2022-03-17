from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'invitation'

urlpatterns = [
    path('', views.login, name='login'),
    path('home',views.home, name ='home'),
    path('main',views.main, name ='main'),
]