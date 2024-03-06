from django.db import models
import datetime

#Category
class Category(models.Model):
    name = models.CharField(max_length=63)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'categories'
    
# Costumers
class Customer(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.first_name + " " + self.last_name
    
    class Meta:
        verbose_name = 'customers'

# All of our products
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.CharField(max_length=255, default='', blank=True, null=True)
    sale = models.BooleanField(default=False)
    image = models.ImageField(upload_to='uploads/product/')
    
    def __str__(self):
        return self.name + " " + str(self.price)
    
    class Meta:
        verbose_name = 'products'
    
# Customer Orders
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=255, default='', blank=True, null=True)
    phone = models.CharField(max_length=15, default='', blank=True, null=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.product.name + " " + self.customer.first_name + " " + str(self.date)
    
    class Meta:
        verbose_name = 'orders'
        