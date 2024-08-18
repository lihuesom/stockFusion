from django.db import models
from django.conf import settings
from django.utils import timezone
from products.models import Product
from users.models import User

class Inventory(models.Model):
    INVENTORY_STATUS = [
        ('delivered', 'Delivered'),
        ('pending', 'Pending'),
        ('returned', 'Returned'),
        ('lost', 'Lost'),
        ('damaged', 'Damaged'),
        ('under_review', 'Under Review'), 
    ]

    product = models.IntegerField()
    owner = models.IntegerField()
    registered_by = models.IntegerField()
    delivery_date = models.DateField()
    serie = models.BigIntegerField()
    status = models.CharField(max_length=50, choices=INVENTORY_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} - {self.owner.username} - {self.serie}"

    class Meta:
        verbose_name = 'Inventory'
        verbose_name_plural = 'Inventory Items'
    
    def get_user(self):
        return User.objects.using('default').get(pk=self.user_id)
    
    def get_product(self):
        return Product.objects.using('default').get(pk=self.product_id)
