from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

market_kind= [
    ("FRUIT & VEGAS", "FRUIT & VEGAS"),
    ("JUICES", "JUICES"),
]
class Market(models.Model):
    love=models.BooleanField(default=False)
    name=models.CharField(max_length=25)
    image=models.ImageField(upload_to='products/')
    kind= models.CharField(choices= market_kind, max_length= 25)
    unit=models.PositiveSmallIntegerField()
    rate=models.DecimalField(max_digits= 3,decimal_places=1)
    price= models.DecimalField(max_digits=4,decimal_places=2)
    discount= models.IntegerField(validators=[MaxValueValidator(99)], default=0)
    selling= models.IntegerField(default=0)
    time= models.TimeField(auto_now=True)
    
    @property
    def latest(self):
        return self.time.hour == 23 
    
    def __str__(self):
        return str(self.name)
    
class Cart(models.Model):
    product= models.ForeignKey(Market, on_delete=models.PROTECT, blank=True, null=True)
    number=models.IntegerField()
    cash= models.DecimalField(max_digits= 4,decimal_places= 2)
    
    def __str__(self):
        return str(self.product)

class Customers(models.Model):
    name= models.ForeignKey(User, on_delete=models.PROTECT,max_length=25)
    email= models.EmailField(max_length=25)
    subscribe= models.BooleanField(default=False)
    cart= models.ManyToManyField(Cart)
    
    def __str__(self):
        return str(self.name)