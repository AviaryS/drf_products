from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=255)
    size = models.IntegerField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()