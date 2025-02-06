from django.db import models
from django.contrib.auth.hashers import make_password


# Create your models here.

class Buyer(models.Model):
    username = models.CharField(max_length=200, unique=True)  # Логин покупателя (уникальный)
    password = models.CharField(max_length=128, default='password')  # Храним зашифрованный пароль
    balance = models.DecimalField(max_digits=10, decimal_places=2)  # Баланс
    age = models.IntegerField()

    class Meta:
        verbose_name='Покупатель'
        verbose_name_plural = 'Покупатели'

    def save(self, *args, **kwargs):
        # Хешируем пароль перед сохранением
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


class Game(models.Model):
    title = models.CharField(max_length=200)  # название игры
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # Цена игры
    size = models.DecimalField(max_digits=10, decimal_places=2)  # Размер файлов игры
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='buyers')
    class Meta:
        verbose_name='Игра'
        verbose_name_plural = 'Игры'
        ordering = ['-cost'] # сортировка по цене
    def __str__(self):
        return self.title
