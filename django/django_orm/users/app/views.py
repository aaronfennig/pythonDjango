from django.shortcuts import render, redirect, HttpResponse
from .models import User

def index(request):
    context = {
        "all_users": User.objects.all()
    }
    return render(request, "index.html", context)

def postUser(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email_address = request.POST['email_address']
    age = request.POST['age']
    if age == "":
        age = None
    User.objects.create(
        first_name = first_name,
        last_name = last_name,
        email_address = email_address,
        age = age
    )
    return redirect("/")
