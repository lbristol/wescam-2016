from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login, views
from django.contrib.auth.forms import UserCreationForm
from forms import *
from django.http import HttpResponse

def index(request):
    if request.user.is_authenticated():
        return dashboard(request)
    else:
        return views.login(request)

# def login_user(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 return dashboard(request)
#             else:
#                 return HttpResponse("Account inactive")
#         else:
#             return HttpResponse("An error occurred logging in")
#     else:
#         return render(request, 'registration/login.html')

def logout_user(request):
    logout(request)
    return HttpResponse("Logged out")

def register_user(request): 
    if request.method == 'POST':
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            Student.objects.create(user=user, email=form.cleaned_data['email'])
            return render(request, "registration/register_complete.html")
        return "Error"
    else:
        form = StudentCreateForm()

        return render(request, 'registration/register.html',{'form':form})

def dashboard(request):
    return render(request, 'dashboard.html')
