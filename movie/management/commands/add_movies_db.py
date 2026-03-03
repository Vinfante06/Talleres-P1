from django.core.management.base import BaseCommand
from django.conf import settings
from movie.models import Movie
import os
import json
class Command(BaseCommand):
    help = 'Load movies from movies.json into the Movie model'

    def handle(self, *args, **kwargs):
        # Construir la ruta absoluta al archivo JSON
        json_file_path = os.path.join(
            settings.BASE_DIR,
            'movie',
            'management',
            'commands',
            'movies.json'
        )

        # Verificar que el archivo exista
        if not os.path.exists(json_file_path):
            self.stdout.write(self.style.ERROR('El archivo movies.json no existe'))
            return

        # Cargar datos desde el archivo JSON
        with open(json_file_path, 'r', encoding='utf-8') as file:
            movies = json.load(file)

        count = 0

        # Recorrer películas (máximo 100 o menos si el JSON tiene menos)
        for movie in movies[:100]:
            exist = Movie.objects.filter(title=movie['title']).first()

            if not exist:
                Movie.objects.create(
                    title=movie['title'],
                    image='movie/images/default.jpg',
                    genre=movie['genre'],
                    year=movie['year'],
                    description=movie.get('plot') or "No description available",
                )
                count += 1

        self.stdout.write(
            self.style.SUCCESS(f'Se agregaron {count} películas correctamente')
        )