from django.urls import path
from applications.inventory.views import *

urlpatterns = [
    path('inventory/', InventoryAPIView.as_view(), name='inventory-list'), 
    path('inventory/<str:pk>/', InventoryAPIView.as_view(), name='inventory-detail'), 
]