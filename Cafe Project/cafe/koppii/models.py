from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Reservations(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Date = models.CharField(max_length=50)
    Time = models.CharField(max_length=50)    
    Person = models.CharField(max_length=50)    
    
class Contacts(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Subject = models.CharField(max_length=50)
    Message = models.CharField(max_length=50)   
    
class signins(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Contact = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    ConfirmPassword = models.CharField(max_length=50)  
class Product(models.Model):
    Name=models.CharField(max_length=150,null=False,blank=False)
    Product_image=models.ImageField(null=True,blank=True)
    Quantity=models.IntegerField(null=False, blank=False)
    Price = models.FloatField(null=False, blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
      
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_cost(self):
        return self.product_qty*self.product.selling_price____


    