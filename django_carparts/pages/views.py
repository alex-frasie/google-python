from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage_view(request, *args, **kwargs):
    #return HttpResponse("<h1 align=center>Welcome to our Car parts warehouse!</h1>")
    return render(request, "home.html", {})