from django.db import models
import uuid

# Create your models here.
class Movie(models.Model):

    GENRE_CHOICES = [
        ('action', 'Action'),
        ('comedy', 'Comedy'),
        ('drama', 'Drama'),
        ('horror', 'Horror'),
        ('romance', 'Romance'),
        ('science_fiction', 'Science Fiction'),
        ('fantasy', 'Fantasy'),

    ]

    uu_id = models.UUIDField(default=uuid.uuid4)
    title = models.CharField(max_lenght=255)
    description = models.TextField()
    release_date = models.Datefield()
    genre = models.Charfield(max_lenght=100, choices=GENRE_CHOICES)
    length = models.PositiveIntegerField()
    image_card = models.ImageField(upload_to='movie_images/')
    image_cover = models.ImageField(upload_to='movie_images/')
    video = models.FileField(upload_to='movie_videos/')
    movie_views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title