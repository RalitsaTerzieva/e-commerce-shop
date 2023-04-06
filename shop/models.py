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