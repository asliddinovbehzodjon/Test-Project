from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *
router = DefaultRouter()
router.register('shopping',ShoppingViewset,basename='shopping')
router.register('users',UserViewset,basename='users')
# router.register('products',Product,basename='products')
urlpatterns = [
    path('',include(router.urls))
]
