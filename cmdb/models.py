from django.db import models

# Create your models here.
class FilmReview(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    time = models.TextField()
    content = models.TextField()
