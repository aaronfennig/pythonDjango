from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def root(request):
    return redirect("/timedisplay")

def index(request):
    context = {
        "day": strftime("%B %d %Y %H:%M %p", gmtime()),
        "time": strftime("%H:%M %p", gmtime())
    }
    print(context)
    return render(request, "index.html", context)
