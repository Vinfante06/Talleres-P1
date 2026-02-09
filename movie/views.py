from django.shortcuts import render 
from django.http import HttpResponse

from models import Movie


def home(request):
    #return HttpResponse('<h1>Welcome to the Movie Reviews Project!</h1>')
    #return render(request, 'home.html')
    #return render(request, 'home.html' , {'name': 'Victor Infante'})
    searchterm = request.GET.get('searMovie')
    movies = Movie.objects.all()
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title_icontains=searchTerm)
    else: 
        movies = Movie.object.all()
    return render(request, 'home.html', {'searchTerm': searchterm, 'movies': movies})


def about(request):
    return render(request, 'about.html')

