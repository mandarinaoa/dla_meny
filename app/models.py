from django.db import models

# Create your models here.
class Product(models.Model):
    name_product = models.CharField(max_length=20)
    price = models.IntegerField()
    quantity = models.IntegerField()
    stars = models.CharField(max_length=20)
    country = models.CharField(max_length=20)