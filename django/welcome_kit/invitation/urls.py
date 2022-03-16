from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'invitation'

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
]