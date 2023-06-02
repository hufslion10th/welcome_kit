from users.models import User, TeamManager
from greet.models import Greet

from django.contrib import auth
from django.contrib.auth import logout

from django.shortcuts import render, redirect

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return redirect('/')


def render_template(request, template_name):
    return render(request, f'invitation/{template_name}.html')


def logout_view(request):
    logout(request)

    return redirect('/')


@method_decorator(csrf_exempt)
def login(request):

    if request.method == "POST":

        user_id = request.POST['username']
        password = '1234'   #password 임의 통일

        user = auth.authenticate(
            request,
            user_id=user_id,
            password=password
        )

        if user is not None:
            auth.login(request, user)

            return redirect ('/')
        
        else:
            context = {
                'error': "Username or Password is incorrect."
            }

            return render(request, "invitation/home.html", context)
    
    else:
        return render(request, "invitation/home.html")

def doctor(request):
    user_id = request.user
    tm = TeamManager.objects.get(tm=user_id.leader)

    s1 = User.objects.get(user_id=user_id.student1)
    s2 = User.objects.get(user_id=user_id.student2)
    if user_id.student3 != None:
        s3 = User.objects.get(user_id=user_id.student3)
    else:
        s3 = "None"

    context  = {
        "leader":user_id.leader,
        "src": tm.src,
        "hi": tm.hi,
        "email": tm.email,
        "department": tm.department,
        "s1":s1,
        "s2":s2,
        "s3":s3
    }

    print(context)

    return render(request, 'invitation/doctor.html', context)

def rollingpaper(request):
    group = User.objects.get(user_id = request.user.get_username())
    rollingpaper_list = Greet.objects.filter(name=group)

    context  = {
        'rollingpaper_list' : rollingpaper_list
    }

    return render(request, 'invitation/rollingpaper.html', context)
