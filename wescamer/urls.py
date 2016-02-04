from django.conf.urls import include, url
from django.contrib import admin
from .views import *


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^register', register_user, name='register'),
    url(r'^dashboard', dashboard, name='dashboard'),
    url(r'^logout', logout_user, name='logout'),
    url(r'^addCrush', add_crush, name='addCrush'),
    url('^', include('django.contrib.auth.urls'))


]
