from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    annotation = models.TextField()
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
# Create your models here.
