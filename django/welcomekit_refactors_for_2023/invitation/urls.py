from . import views

from django.urls import path

app_name = 'invitation'

urlpatterns = [

    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),

    path('doctor/',views.doctor, name ='doctor'),
    path('rollingpaper/',views.rollingpaper, name ='rollingpaper'),
    path('<str:template_name>/', views.render_template),
]