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

    def put(self, request):
        data = request.data  # Expecting a list of updates
        if not isinstance(data, list):
            return Response({"error": "Request data must be a list of updates"}, status=status.HTTP_400_BAD_REQUEST)
        
        updated_items = []
        errors = []

        for item in data:
            pk = item.get('_id')
            if not pk:
                errors.append({"error": "Item must contain '_id'"})
                continue
            
            try:
                inventory = InventoryService.update_inventory(pk, item)
                updated_items.append(InventorySerializer(inventory).data)
            except Exception as e:
                errors.append({"_id": pk, "error": str(e)})

        if errors:
            return Response({"updated_items": updated_items, "errors": errors}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"updated_items": updated_items}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        inventory = get_object_or_404(Inventory, pk=pk)
        inventory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
