from django.shortcuts import render
from django.http import HttpResponse
from flaming.AppFlaming.models import GestionGanancias
# Create your views here.
def GestionRender(request):
    listaProductos = GestionGanancias.objects.all()
    return render(request, 'adminlte/gestion/gestionProductos.html',{'listaProductos': listaProductos})