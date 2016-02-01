from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login, views
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

def index(request):
    return HttpResponse("Wescam 2016")