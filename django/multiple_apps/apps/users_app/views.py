# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import HttpResponse, redirect

# Create your views here.
def index(request):
    return HttpResponse("placeholder to later display all the list of users")

def register(request):
    return HttpResponse("placeholder to display a new form to create a new user")
    

def login(request, user_id):
    return HttpResponse("placeholder to display user {}".format(user_id))

