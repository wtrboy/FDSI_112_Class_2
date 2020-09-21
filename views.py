from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def test(request):
    return HttpResponse("Test Page")

def about(request):
    return HttpResponse("M. Lane Thompson")