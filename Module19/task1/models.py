from django.db import models


# Create your models here.

class Buyer(models.Model):
    username = models.CharField(max_length=200)  # логин покупателя
    balance = models.DecimalField(max_digits=10, decimal_places=2)  # Баланс
    age = models.IntegerField()

    def __str__(self):
        return self.username


class Game(models.Model):
    title = models.CharField(max_length=200)  # название игры
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # Цена игры
    size = models.DecimalField(max_digits=10, decimal_places=2)  # Размер файлов игры
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='buyers')

    def __str__(self):
        return self.title
