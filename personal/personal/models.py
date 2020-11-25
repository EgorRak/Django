from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.ForeignKey('Country',on_delete=models.CASCADE)

class Genre(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    name = models.CharField(max_length=100)
    year_issued = models.PositiveSmallIntegerField()
    authors = models.ManyToManyField("Author")
    pages_count = models.PositiveSmallIntegerField()
    genres = models.ManyToManyField("Genre")

class BookCopy(models.Model):
    book = models.ForeignKey('Book',on_delete=models.CASCADE)
    order_number = models.PositiveSmallIntegerField()







"""1. Создать models.py, в котором описать модели системы библиотеки:
Country: name (unique).
Author: first_name, last_name, country (FK -> Country).
Genre: name
Book: name, author (M2M -> Author), year_issued, pages_count, genres (M2M -> Genre).
BookCopy: book (FK->Book), order_number.
"""