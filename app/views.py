from .serializers import *
from .models import Shopping,Product
from rest_framework import viewsets,status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .permissions import IsStaff
# Create your views here.
class ShoppingViewset(viewsets.ModelViewSet):
     permission_classes = (IsStaff,)
     queryset = Shopping.objects.all()
     def list(self,request):
          serializer = ShoppingSerializer(self.queryset,many=True)
          return Response(serializer.data)
          
     def create(self, request):
          
          serializer = ShoppingSerializer(data = request.data)
          return Response(serializer.data)
class UserViewset(viewsets.ModelViewSet):
     queryset = User.objects.all()
     serializer_class = UserSerializer
class ProductViewset(viewsets.ModelViewSet):
     queryset = Product.objects.all()
     serializer_class = ProductSerializer
     
      