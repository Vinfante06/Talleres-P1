import matplotlib.pyplot as plt
import matplotlib
import io
import urllib, base64
from django.shortcuts import render 
from django.http import HttpResponse

from .models import Movie


def home(request):
    #return HttpResponse('<h1>Welcome to the Movie Reviews Project!</h1>')
    #return render(request, 'home.html')
    #return render(request, 'home.html' , {'name': 'Victor Infante'})
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else: 
        movies = Movie.objects.all()
    return render(request, 'home.html', {'searchTerm': searchTerm, 'movies': movies})


def about(request):
    return render(request, 'about.html')


def statistics_view(request):
    matplotlib.use('Agg')

    
    all_movies = Movie.objects.all()

    
    movie_counts_by_year = {}

    for movie in all_movies:
        year = movie.year if movie.year else "None"

        if year in movie_counts_by_year:
            movie_counts_by_year[year] += 1
        else:
            movie_counts_by_year[year] = 1

    # Ancho de las barras
    bar_width = 0.5


    bar_positions = range(len(movie_counts_by_year))

    plt.bar(
        bar_positions,
        movie_counts_by_year.values(),
        width=bar_width,
        align='center'
    )

    plt.title('Movies per year')
    plt.xlabel('Year')
    plt.ylabel('Number of movies')
    plt.xticks(
        bar_positions,
        movie_counts_by_year.keys(),
        rotation=90
    )

    
    plt.subplots_adjust(bottom=0.3)

    
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    
    image_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return render(
        request,
        'statistics.html',
        {'graphic': graphic}
    )

def statistics_view(request):
    matplotlib.use('Agg')

    all_movies = Movie.objects.all()

    # =============================
    # 📊 GRÁFICA 1: Movies per year
    # =============================
    movie_counts_by_year = {}

    for movie in all_movies:
        year = movie.year if movie.year else "None"
        if year in movie_counts_by_year:
            movie_counts_by_year[year] += 1
        else:
            movie_counts_by_year[year] = 1

    plt.figure()
    bar_positions = range(len(movie_counts_by_year))
    plt.bar(
    bar_positions,
    movie_counts_by_year.values()
)
    plt.xticks(
    bar_positions,
    movie_counts_by_year.keys(),
    rotation=90
)
    plt.title('Movies per year')
    plt.xlabel('Year')
    plt.ylabel('Number of movies')
    plt.xticks(rotation=90)
    plt.subplots_adjust(bottom=0.3)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    graphic_year = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()
    plt.close()


    # =============================
    # 📊 GRÁFICA 2: Movies per genre
    # =============================
    movie_counts_by_genre = {}

    for movie in all_movies:
        if movie.genre:
            first_genre = movie.genre.split(',')[0].strip()
        else:
            first_genre = "None"

        if first_genre in movie_counts_by_genre:
            movie_counts_by_genre[first_genre] += 1
        else:
            movie_counts_by_genre[first_genre] = 1

    plt.figure()
    plt.bar(movie_counts_by_genre.keys(), movie_counts_by_genre.values())
    plt.title('Movies per Genre')
    plt.xlabel('Genre')
    plt.ylabel('Number of movies')
    plt.xticks(rotation=90)
    plt.subplots_adjust(bottom=0.3)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    graphic_genre = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()
    plt.close()

    return render(request, 'statistics.html', {
        'graphic_year': graphic_year,
        'graphic_genre': graphic_genre
    })

    return render(request, 'statistics.html', {'graphic': graphic})

def signup_view(request):
    email = request.POST.get('email')
    return render(request, 'signup.html', {'email': email})