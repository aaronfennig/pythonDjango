from django.shortcuts import render, redirect, HttpResponse
from .models import *

def root(request):
    context = {
        "dojos": Dojo.objects.all()
    }
    return render(request, "index.html", context)

def postDojo(request):
    name = request.POST['name']
    city = request.POST['city']
    state = request.POST['state']
    Dojo.objects.create(
        name = name,
        city = city,
        state = state
    )
    return redirect("/")

def postNinja(request):
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    dojo = request.POST["dojo"]
    Ninja.objects.create(
        first_name = first_name,
        last_name = last_name,
        dojo = Dojo.objects.get(id = int(dojo))
    )
    return redirect("/")

def deleteNinja(request):
    id = request.POST["id"]
    to_delete = Ninja.objects.get(id = int(id))
    to_delete.delete()
    return redirect("/")

def deleteDojo(request):
    id = request.POST["id"]
    to_delete = Dojo.objects.get(id = int(id))
    to_delete.delete()
    return redirect("/")

