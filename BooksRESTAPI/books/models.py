from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    objects = models.Manager()

    title = models.CharField(max_length=300)
    authors = models.ManyToManyField('Author')
    published_date = models.CharField(max_length=4)
    categories = models.ManyToManyField('Category')
    average_rating = models.IntegerField(null=True)
    ratings_count = models.IntegerField(null=True)
    thumbnail = models.URLField(max_length=300)

    def __str__(self):
        return self.title
