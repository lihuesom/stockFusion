from django.shortcuts import get_object_or_404
from ..models import *
from applications.products.models import Product
from applications.users.models import User
from bson import ObjectId
from django.contrib.auth.hashers import make_password

class InventoryService:
    @staticmethod
    def create_inventory(data):
        product = get_object_or_404(Product, pk=data.get('product'))
        
        owner, created = User.objects.get_or_create(
            identification=data.get('identification'),
            defaults={
                'email': data.get('email'),
                'first_name': data.get('first_name'),
                'last_name': data.get('last_name'),
                'cellphone': data.get('cellphone'),
                'document_type': data.get('document_type'),
                'identification':data.get('identification')
            }
        )
        
        if not created:
            owner.email = data.get('email')
            owner.first_name = data.get('first_name')
            owner.last_name = data.get('last_name')
            owner.cellphone = data.get('cellphone')
            owner.document_type = data.get('document_type')
            owner.save()
        
        registered_by = get_object_or_404(User, email=data.get('registered_by'))
        
        inventory = Inventory.objects.create(
            product={"pk": product.pk, "name": product.name},
            owner={
                "pk": owner.pk, 
                "fullname": f'{owner.first_name} {owner.last_name}',
                "identification": owner.identification
                },
            registered_by={"pk": registered_by.pk, "identification": registered_by.identification},
            delivery_date=data.get('delivery_date'),
            approved_by = {},
            serie=str(data.get('serie')),
            status='pending'
        )
        return inventory

    @staticmethod
    def update_inventory(pk, data):
        object_id = ObjectId(pk)
        
        approved_by = get_object_or_404(User, email="example@example.com")
        approved_by = {"pk": approved_by.pk, "identification": approved_by.identification}
            
        instance = get_object_or_404(Inventory, _id=object_id)
        instance.approved_by = approved_by or  instance.approved_by
        instance.status = data.get('status', instance.status)
        instance.save()
        return instance
