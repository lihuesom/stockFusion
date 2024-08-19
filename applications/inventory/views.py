from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Inventory
from .serializers import InventorySerializer
from .services.inventoryService import InventoryService
from django.shortcuts import get_object_or_404
from .forms import InventoryForm

class InventoryAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            inventory = get_object_or_404(Inventory, pk=pk)
            serializer = InventorySerializer(inventory)
        else:
            inventory = Inventory.objects.all()
            print(inventory)
            serializer = InventorySerializer(inventory, many=True)
        return Response(serializer.data)

    def post(self, request):
        form = InventoryForm(request.data)
        if form.is_valid():
            data = form.cleaned_data
            inventory = InventoryService.create_inventory(data)
            serializer = InventorySerializer(inventory)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        inventory = InventoryService.update_inventory(pk, request.data)
        serializer = InventorySerializer(inventory)
        return Response(serializer.data)

    def delete(self, request, pk):
        inventory = get_object_or_404(Inventory, pk=pk)
        inventory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
