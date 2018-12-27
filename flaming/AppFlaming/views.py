from django.shortcuts import render
from django.http import HttpResponse
from flaming.AppFlaming.models import GestionGanancias, StockProducto
# Create your views here.

def GestionRender(request):
    listaProductos = GestionGanancias.objects.all()
    for producto in listaProductos:
        producto.stockInicial = ReturnStock(producto)
    return render(request, 'adminlte/gestion/gestionProductos.html',{'listaProductos': listaProductos})

def ReturnStock(producto):
    listaStock = StockProducto.objects.all()
    totalStock = 0
    for stock in listaStock:
        if stock.producto == producto.producto:
           totalStock += stock.cantidadStock
        
    return totalStock