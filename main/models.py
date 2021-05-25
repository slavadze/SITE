from django.db import models


class Product(models.Model):

    available_CHOICES = (
        ('1', 'В наличии'),
        ('2', 'Под заказ'),
    )

    title = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    currency = models.CharField(max_length=3)
    availability = models.CharField(max_length=30, choices=available_CHOICES, default='1')
    img = models.ImageField(upload_to='static/images/', null=True, blank=True, default='static/images/default.jpg')

    # выводит title в админке / название товаров
    def __str__(self):
        return f'{self.title}'