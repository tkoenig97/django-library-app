from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return (f"{self.first_name} {self.last_name}")
    
class Genre(models.Model):
    title = models.CharField(max_length=250)
    
class Book(models.Model):
    title = models.CharField(max_length=250)
    quantity = models.IntegerField(default=1)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    authors = models.ManyToManyField(Author, related_name="book")