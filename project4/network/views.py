from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

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

def getHistoricalData(request):
    accountKey = User.objects.GET["username"=asd]

    transaction_url = 'https://849rs099m3.execute-api.ap-southeast-1.amazonaws.com/techtrek/transactions/view'

    headers = {
        'x-api-key': 'rcqYXzQ9PY1rQtUNJB9X56JOvnQWnf27S09nX8Rh',
        'Content-Type': 'application/json',
    }
    payload={
        'accountKey': accountKey
    }

    #data = json.loads(r.post(transaction_url, headers=headers, json = payload).content)
    data = r.post(transaction_url, headers=headers, json = payload).content

    return render(request, "network/register.html", {
        "message": data
    })

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


def asset(request):
    myAccount = User.objects.get(username=request.GET['username']
    # API function here


    # Return Json for Now
    pass

def transaction(request):
    myAccount = User.objects.get(username=request.GET['username']
    # API function here


    # Return Json for Now
    pass
