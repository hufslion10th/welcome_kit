from re import template
from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth import authenticate, login
from .forms import LoginForm

# Create your views here.
class LoginView(FormView):
    
    template_name = 'invitation/index.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        user_id = form.cleaned_data.get("user_id")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=user_id, password=password)
        
        if user is not None:
            self.request.session['user_id'] = user_id
            login(self.request, user)

        return super().form_valid(form)
