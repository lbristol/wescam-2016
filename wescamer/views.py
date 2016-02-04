from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login, views
from django.contrib.auth.forms import UserCreationForm
from forms import *
from django.http import HttpResponse
from models import *

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
    try:
        received_crushes = Crush.objects.filter(crushee=request.user)
    except Crush.DoesNotExist:
        received_crushes = []
    try:
        sent_crushes = Crush.objects.filter(crusher=request.user)
    except Crush.DoesNotExist:
        sent_crushes = []
    return render(request, 'dashboard.html', {'received_crushes':received_crushes, 'sent_crushes' :sent_crushes})

def add_crush(request):
    if request.method == 'POST':
        form = AddCrush(request.POST)
        if form.is_valid():
            crush_username = form.cleaned_data['crush_username']
            c = Student.objects.get(email=crush_username+"@wesleyan.edu").user
            print c
            # print username
            # cr = Crush.objects.filter(crusher=c, crushee=request.user)
            if Crush.objects.filter(crusher=c, crushee=request.user).count() > 0: #A reciprocating crush
                cr = Crush.objects.get(crusher=c, crushee=request.user)
                cr.reciprocated=True
                cr.save()
            else: #A new crush
                crush = Crush.objects.create(crusher=request.user, crushee=c, reciprocated=False, nickname = "hidden")

            return HttpResponse("Added user " + crush_username)
    print form
    return HttpResponse("An error occurred adding crush")

