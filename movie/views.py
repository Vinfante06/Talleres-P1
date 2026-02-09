from django.shortcuts import render 
from django.http import HttpResponse

from .models import Movie


def home(request):
    #return HttpResponse('<h1>Welcome to the Movie Reviews Project!</h1>')
    #return render(request, 'home.html')
    #return render(request, 'home.html' , {'name': 'Victor Infante'})
    searchTerm = request.GET.get('searMovie')
    movie = Movie.objects.all()
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movie = Movie.objects.filter(title__icontains=searchTerm)
    else: 
        movie = Movie.objects.all()
    return render(request, 'home.html', {'searchTerm': searchTerm, 'movie': movie})


def about(request):
    return render(request, 'about.html')

