from django.db import models

# Create your models here.
class Product(models.Model):
    type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    sale = models.BooleanField(default=False)
    image = models.ImageField(upload_to='products', null=True, blank=True)
    
    def __str__(self):
        return self.name