from djongo import models
class Inventory(models.Model):
    INVENTORY_STATUS = [
        ('delivered', 'Delivered'),
        ('pending', 'Pending'),
        ('returned', 'Returned'),
        ('lost', 'Lost'),
        ('damaged', 'Damaged'),
        ('under_review', 'Under Review'), 
    ]
    
    _id = models.ObjectIdField(primary_key=True)
    product = models.JSONField()
    owner = models.JSONField()
    registered_by = models.JSONField()
    approved_by = models.JSONField(null=True, blank=True)
    delivery_date = models.DateField()
    serie = models.BigIntegerField()
    status = models.CharField(max_length=50, choices=INVENTORY_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Inventory'
        verbose_name_plural = 'Inventory Items'
