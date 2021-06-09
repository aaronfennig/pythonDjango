from django.shortcuts import render, redirect, HttpResponse

def survey(request):
    return render(request, "index.html")

def submit(request):
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    print("***************",request.session)
    return redirect("/success")

def success(request):
    print("***************",request.session)
    return render(request, "success.html")


# Create your views here.
