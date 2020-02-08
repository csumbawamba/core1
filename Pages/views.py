from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello world</h1>")

def contact(request):
    return HttpResponse("<h1>Contact</h1>")

def about(request):
    return HttpResponse("<h1>About</h1>")    