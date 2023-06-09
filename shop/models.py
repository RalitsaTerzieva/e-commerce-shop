from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField(default=0.00)
    discount_price = models.FloatField(default=0.00)
    category = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    image = models.CharField(max_length=300)
    
    def __str__(self):
        return self.title
    
class Order(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    price = models.FloatField(default=0.00)
    
    def __str__(self):
        return self.name
    