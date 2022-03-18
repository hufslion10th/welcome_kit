from re import template

# Create your views here.
#from .forms import LoginForm
#from django.contrib.auth import login, authenticate
#from django.views.generic import FormView


from django.shortcuts import render, redirect
from django.contrib import auth
from users.models import User

def login(request):
    if request.method == "POST":
        user_id = request.POST['username']
        password = '1234'

        user = auth.authenticate(
            request, user_id=user_id, password=password
        )

        if user is not None:
            auth.login(request, user)
            return redirect ('invitation:home')
        else:
            return render(request, "invitation/index.html", {
            'error': "Username or Password is incorrect.",
        })
    else:
        return render(request, "invitation/index.html")

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('/')

def home(request):
    return render(request, 'invitation/index.html')

def main(request):
    return render(request, 'invitation/main.html')

def roadmap_FE(request):
    return render(request, 'invitation/roadmap_FE.html')

def roadmap_BE(request):
    return render(request, 'invitation/roadmap_BE.html')

def roadmap_PMD(request):
    return render(request, 'invitation/roadmap_PMD.html')

def roadmap_today(request):
    return render(request, 'invitation/roadmap_today.html')

def doctor(request):
    return render(request, 'invitation/doctor.html')

def bingo1(request):
    return render(request, 'invitation/bingo1.html')

def bingo2(request):
    return render(request, 'invitation/bingo2.html')

def bingo3(request):
    return render(request, 'invitation/bingo3.html')

def bingo4(request):
    return render(request, 'invitation/bingo4.html')

def bingo5(request):
    return render(request, 'invitation/bingo5.html')

def agit(request):
    return render(request, 'invitation/agit.html')

def rollingpaper(request):
    return render(request, 'invitation/rollingpaper.html')