# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import random
from datetime import datetime

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'log' not in request.session:
        request.session['log'] = []
    return render(request, 'ninja_app/index.html')

def process_money(request):
    building = request.POST['building']
    earned_gold = 0

    if building == 'farm':
        earned_gold = random.randint(10,20)
    elif building == 'cave':
        earned_gold = random.randint(5,10)
    elif building == 'house':
        earned_gold = random.randint(2,5)
    elif building == 'casino':
        if request.session['gold']<1:
            request.session['log'].append('you can not go into the casino if you do not have any gold.({})'.format(datetime.now()))
            return redirect('/')

        earned_gold = random.randint(-50, 50)
        if earned_gold<0:
            if request.session['gold']-abs(earned_gold)>0:
                request.session['log'].append('entered a casino and lost {}. ({})'.format(earned_gold, datetime.now()))
            else:
                request.session['log'].append('entered a casino and lost all of your gold! ({})'.format(datetime.now()))
        else:
            request.session['log'].append('entered a casino and won {}. ({})'.format(earned_gold, datetime.now()))
        session['gold']+=earned_gold
        return redirect('/')

    request.session['gold']+=earned_gold
    request.session['log'].append('earned {} gold from the {}. ({})'. format(earned_gold, building, datetime.now()))
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')
