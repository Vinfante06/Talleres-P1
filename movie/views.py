from django.shortcuts import render 
from django.http import HttpResponse

def home(request):
    #return HttpResponse('<h1>Welcome to the Movie Reviews Project!</h1>')
    #return render(request, 'home.html')
    return render(request, 'home.html' , {'name': 'Grem Lim'})

def about(request):
    return HttpResponse("This is the about page.")

