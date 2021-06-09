from django.shortcuts import render, HttpResponse, redirect
import random

def root(request):
    if "gold" in request.session:
        pass
    else:
        request.session['gold'] = 0
    if "activity_log" in request.session:
        pass
    else:
        request.session['activity_log'] = []
    print (request.session['gold'], request.session['activity_log'])
    return render(request, "index.html")

def process_money(request):
    if request.POST['type'] == "farm":
        amount = random.randint(10, 20)
        request.session["gold"] += amount
        request.session["activity_log"].append({'activity': request.POST['type'], 'amount': amount, 'did_gain': True})
    elif request.POST['type'] == "cave":
        amount = random.randint(5,10)
        request.session["gold"] += amount
        request.session["activity_log"].append({'activity': request.POST['type'], 'amount': amount, 'did_gain': True})
    elif request.POST['type'] == "house":
        amount = random.randint(2,5)
        request.session["gold"] += amount
        request.session["activity_log"].append({'activity': request.POST['type'], 'amount': amount, 'did_gain': True})
    else:
        amount = random.randint(0,50)
        does_win= random.randint(0,1)
        if does_win == 0:
            request.session["gold"] -= amount
            request.session["activity_log"].append({'activity': request.POST['type'], 'amount': amount, 'did_gain': False})
        else:
            request.session["gold"] += amount
            request.session["activity_log"].append({'activity': request.POST['type'], 'amount': amount, 'did_gain': True})
    return redirect("/")

def reset_game(request):
    del request.session['gold']
    del request.session['activity_log']
    return redirect('/')
