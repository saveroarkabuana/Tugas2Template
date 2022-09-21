from django.db import models

# Create your models here.
class MyWatchList(models.Model):
    watched = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    rating = models.IntegerField()
    release_date = models.CharField(max_length=255)
    review = models.TextField()