from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=33)
    author = models.CharField(max_length=55)
    year = models.PositiveIntegerField()
    price = models.FloatField()

    def __str__(self):
        return self.title