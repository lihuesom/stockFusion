from django import forms
from applications.products.models import Product

class InventoryForm(forms.Form):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    cellphone = forms.IntegerField()
    identification = forms.CharField(max_length=255)
    document_type = forms.ChoiceField(choices=[
            ('CC', 'Cédula de Ciudadanía'),
            ('TI', 'Tarjeta de Identidad'),
            ('PAS', 'Pasaporte'),
            ('NIT', 'Número de Identificación Tributaria'),
        ])
    product = forms.IntegerField()
    serie = forms.IntegerField()
    delivery_date = forms.DateField()
    registered_by = forms.CharField(max_length=255)

    def clean(self):
        cleaned_data = super().clean()
        product_id = cleaned_data.get("product")

        if not Product.objects.filter(pk=product_id).exists():
            raise forms.ValidationError("Product does not exist.")

        
