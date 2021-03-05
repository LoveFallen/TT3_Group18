from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

import requests as r
import json

from .models import User


def index(request):
    return render(request, "network/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def asset(request):
    myAccount = User.objects.get(username=request.user)
    # API function here


    # Return Json for Now
    return JsonResponse({})

def transaction(request):
    
    myAccount = User.objects.get(username=request.user)

    # API Function
    transaction_url = 'https://849rs099m3.execute-api.ap-southeast-1.amazonaws.com/techtrek/transactions/view'
    headers = {
        'x-api-key': 'rcqYXzQ9PY1rQtUNJB9X56JOvnQWnf27S09nX8Rh',
        'Content-Type': 'application/json',
    }
    payload={
        'accountKey': myAccount.accountKey
    }
    
    data = json.loads(r.post(transaction_url, headers=headers, json = payload).content)
    
    return render(request, "network/transaction_history.html",{
        'assets': data,
        'user': myAccount,
    })


def accKey(request):
    myAccount = User.objects.get(username=request.user)

    return JsonResponse({
        'accountKey': myAccount.accountKey
    })


def profile(request):
    return JsonResponse({
        'msg': 'Get Profile',
    })


def buy(request):
    myAccount = User.objects.get(username=request.user)
    
    return render(request, "network/buy_asset.html",{
    })


def sell(request):
    myAccount = User.objects.get(username=request.user)
    
    return render(request, "network/sell_asset.html",{
    })
