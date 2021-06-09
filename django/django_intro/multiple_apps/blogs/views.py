from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

def root(request):
    return redirect("/blogs")

def index(request):
    return HttpResponse("Placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/blogs")

def show(request, number):
    return HttpResponse(f"placeholder to display blog number: {number}")

def edit(request, number):
    return HttpResponse(f"placeholder to edit blog: {number}")

def destroy(request, number):
    return redirect("/blogs")

def showAll(request):
    allBlogs = {
        "title": "My first blog",
        "content": "Sit mollit dolor quis adipisicing eu ullamco ipsum dolore officia fugiat. Nulla dolor fugiat eu sunt veniam ad consectetur irure in veniam nostrud nostrud nostrud nisi. Lorem ex sunt nulla eu mollit eu mollit nulla eiusmod culpa aliqua amet ex. Sint aliqua fugiat laboris consequat aute commodo pariatur fugiat eiusmod eu commodo."
    }
    return JsonResponse(allBlogs)


# Create your views here.
