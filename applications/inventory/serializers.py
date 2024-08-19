from rest_framework import serializers
from .models import *
from collections import OrderedDict

class InventorySerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    owner = serializers.SerializerMethodField()
    registered_by = serializers.SerializerMethodField()
    approved_by = serializers.SerializerMethodField()
    
    class Meta:
        model = Inventory
        fields = '__all__'
    
    def get_product(self, obj):
        return self.parse_ordered_dict(obj.product)

    def get_owner(self, obj):
        return self.parse_ordered_dict(obj.owner)

    def get_registered_by(self, obj):
        return self.parse_ordered_dict(obj.registered_by)

    def get_approved_by(self, obj):
        return self.parse_ordered_dict(obj.approved_by)

    def parse_ordered_dict(self, value):
        if isinstance(value, str) and value.startswith('OrderedDict'):
            clean_str = value.replace('OrderedDict(', '').rstrip(')')
            # Convertir a diccionario
            return dict(eval(clean_str))
        return value