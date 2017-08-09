# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
import string
from django.shortcuts import render, redirect

def random_word(n):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))

# Create your views here.
def index(request):
    try:
        request.session['counter']
    except KeyError:
        request.session['counter'] = 0

    return render(request, "random_word_app/index.html")

def generate(request):
    request.session['counter'] += 1
    request.session['word'] = random_word(10)
    return redirect('/')

def reset(request):
    del request.session['counter']
    del request.session['word']
    return redirect('/')

