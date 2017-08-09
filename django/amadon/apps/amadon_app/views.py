# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from product import items

# Create your views here.
def index(request):
    if 'last_transaction' in request.session:
        del request.session['last_transaction']

    context = {
        'items':items
    }
    return render(request, 'amadon_app/index.html', context)

def buy(request, item_id):
    #cost, total_cost, count(quantity) --- sessions - cost, count, total_cost


    for item in items:
            if item['id'] == int(item_id):
                cost = item['price'] * int(request.POST['quantity'])

    try:
        request.session['total_cost']
    except KeyError:
        request.session['total_cost'] = 0

    try:
        request.session['quantity']
    except KeyError:
        request.session['quantity'] = 0

    request.session['quantity'] += int(request.POST['quantity'])
    request.session['total_cost'] += cost
    request.session['last_transaction'] = cost

    # print request.session['quantity']
    # print request.session['total_cost']
    # print request.session['last_transaction']

    return redirect('/checkout')


def checkout(request):
    return render(request, 'amadon_app/checkout.html')
