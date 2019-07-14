from django.db import models

# Create your models here.
class Article(models.Model):
    id = models.AutoField(primary_key=True)
    categories = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    time = models.DateTimeField()
    content = models.TextField()
