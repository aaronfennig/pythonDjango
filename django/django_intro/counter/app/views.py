from django.shortcuts import render, redirect, HttpResponse

def index(request):
    print("session currently is: counter:",request.session["counter"],"actual counter:", request.session["actual_count"])
    if 'counter' in request.session:
        request.session['counter'] = request.session['counter'] +1
    else:
        request.session['counter'] = 1
    if "actual_count" in request.session:
        request.session['actual_count'] = request.session['actual_count'] +1
    else:
        request.session['actual_count'] = 1

    print(request.session['counter'])
    return render(request, 'index.html')

def destroy(request):
    del request.session['counter']
    request.session["counter"] = -1
    return redirect('/')

def plustwo(request):
    request.session["counter"] = request.session["counter"] +1
    return redirect('/')

def plusx(request):
    request.session["counter"] = request.session["counter"] + int(request.POST["numInput"])
    return redirect('/')
