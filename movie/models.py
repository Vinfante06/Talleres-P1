from django.db import models

class Movie(models.Model):
    title= models.CharField(max_length=200)
    description= models.CharField(max_length=1000)
    image= models.ImageField(upload_to= 'media/movie/images/')  
    url = models.URLField(blank=True)
    genre = models.CharField(blank=True, max_length=250)
    year = models.IntegerField(blank=True, null=True)
    
    def __str__(self):  return self.title

    
# Create your models here.
