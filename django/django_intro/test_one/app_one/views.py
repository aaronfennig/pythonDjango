from django.shortcuts import render,redirect, HttpResponse

def index(request):
    context = {
        "name": "Noelle",
        "favorite_color": "turquoise",
        "pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, "index.html", context)

def csrf(request):
    return render(request, "csrf.html")

def create_user(request):
    print("Got Post Info....................")
    print(request.POST)
    name_from_form = request.POST['name']
    email_from_form = request.POST['email']
    request.session = request.POST
    print("*****************",request.session)
    return render(request, "show.html")

def show_page(request):
    render(request, "show.html")

# Create your views here.
