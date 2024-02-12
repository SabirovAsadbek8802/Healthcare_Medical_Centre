from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def driver(request):
    return render(request, "driver.html")

def landing(request):
    return render(request, "landing.html")

def partner(request):
    return render(request, "partner.html")