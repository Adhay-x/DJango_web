from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length= 20)
    price = models.DecimalField(decimal_places = 2, max_digits=50)
    quantity = models.CharField(max_length=1024)
    quality = models.CharField(max_length=50)
    image = models.CharField(max_length=1024, default = True)
    desc = models.TextField()
