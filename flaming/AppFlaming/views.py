from django.shortcuts import render
from django.http import HttpResponse
from flaming.AppFlaming.models import GestionGanancias, StockProducto

# Import Formularios
from .forms import ProovedorForm, ProductoForm

# Import Modelos
from .models import Proovedor,Producto,

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

def AltaProveedor(request):
    listaProveedores = Proveedor.objects.all()
    if request.method == 'POST':
        formProveedor = ProovedorForm(request.POST)
        if formProveedor.is_valid():
            proveedor = formProveedor.save(commit=False)
            proveedor.save()
            # Retornar alguna URL 
            return HttpResponseRedirect('/')
    else:
        formProveedor = ProovedorForm()
        # Retornar alguna URL 
    return render(request, '/', {'formProveedor': formProveedor, 'listaProveedores': listaProveedores})


def AltaProducto(request):
    listaProductos = Producto.objects.all()

    if request.method == 'POST':
        formProducto = ProductoForm(request.POST)
        if formProducto.is_valid():
            producto = formProducto.save(commit=False)
            producto.save()
            # Retornar alguna URL 
            return HttpResponseRedirect('/')
    else:
        formProducto = ProovedorForm()
        # Retornar alguna URL 
    return render(request, '/', {'formProducto': formProducto, 'listaProductos': listaProductos})

