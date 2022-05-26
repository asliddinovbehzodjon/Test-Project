from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
     name = models.CharField(max_length=500)
     cost = models.IntegerField()
     def __str__(self):
          return self.name
class Shopping(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='shopping')
     product = models.ForeignKey(Product,on_delete=models.CASCADE)
     quantity = models.IntegerField()
     def __str__(self):
          return self.user.username