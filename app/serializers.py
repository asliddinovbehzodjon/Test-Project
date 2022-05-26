from rest_framework import serializers
from .models import Product,Shopping
from django.contrib.auth.models import User
class ShoppingSerializer(serializers.ModelSerializer):
     class Meta:
          model = Shopping
          fields = "__all__"
class UserSerializer(serializers.ModelSerializer):
     shopping = ShoppingSerializer(many=True,read_only = True)
     class Meta:
          model = User
          fields =['id','username','password','shoppings']
class ProductSerializer(serializers.ModelSerializer):
     class Meta:
          model = Product
          fields = "__all__"
     
