from django.shortcuts import render, redirect, HttpResponse
import random

def index(request):
    if 'the_number' in request.session:
        pass
    else:
        request.session['the_number'] = random.randint(1,100)
    print(request.session['the_number'])
    return render(request, "index.html")

def guess(request):
    print(request.POST['userGuess'])
    if int(request.POST['userGuess']) > int(request.session['the_number']):
        return redirect('/toohigh')
    elif int(request.POST['userGuess']) < int(request.session['the_number']):
        return redirect('/toolow')
    else:
        return redirect('/youwin')

def too_high(request):
    return render(request, "too_high.html")

def too_low(request):
    return render(request, "too_low.html")

def you_win(request):
    return render(request, "you_win.html")

def reset(request):
    del request.session['the_number']
    return redirect('/')



