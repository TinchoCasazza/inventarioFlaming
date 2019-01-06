from django import forms
from django.forms import ModelForm

from .models import Proovedor, Producto

class ProveedorForm(ModelForm):
    class Meta:
        model = Proveedor
        fields = 'nombreProovedor', 'descripcionProovedor', 'direccionProovedor', 'telefonoProovedor')

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ('nombreProducto','precioProducto','proovedor')
