from django.contrib import admin
from flaming.AppFlaming.models import Producto,Proovedor,StockProducto,GestionGanancias
# Register your models here.

admin.register(Producto,Proovedor,StockProducto,GestionGanancias)(admin.ModelAdmin)