from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    issued_date = models.DateField()
    expiry_date = models.DateField(blank=True, null=True)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name