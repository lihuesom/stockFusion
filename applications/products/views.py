from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import *

class ProductListView(APIView):

    def get(self, request, *args, **kwargs):
        products = Product.objects.filter(status=True)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
