from django.db import models
from cart.models import Cart, CartItem

class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Brand(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Color(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    price = models.IntegerField()
    promotion = models.DecimalField(max_digits=10, decimal_places=1)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    quantity = models.IntegerField()
    description = models.TextField(max_length=2551)

    def __str__(self):
        return self.title

