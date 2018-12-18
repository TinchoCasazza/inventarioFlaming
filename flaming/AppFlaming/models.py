from django.db import models
import datetime
# Create your models here

class Proovedor(models.Model):
    nombreProovedor = models.CharField(blank=False, max_length=60)
    descripcionProovedor = models.TextField(blank= True)
    direccionProovedor = models.CharField(blank=True, max_length=60)
    telefonoProovedor = models.IntegerField(null=True, blank =True)

    def __string__(self):
        return (self.nombreProovedor)

class Producto(models.Model):
    nombreProducto = models.CharField(blank=False, max_length=60)
    precioProducto = models.FloatField(null=True)
    proovedor = models.ForeignKey(Proovedor, on_delete=models.CASCADE)

    def __string__(self):
        return (self.nombreProducto)

class StockProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete= models.CASCADE)
    fechaReposicion = models.DateField(default = datetime.date.today, editable = True)
    cantidadStock = models.IntegerField(null=False, default=0)

class GestionGanancias(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    stockInicial = models.IntegerField(null = True)
    compras = models.IntegerField(null = True)
    existenciaFinal = models.IntegerField(null = True)
    costoFinal = models.FloatField(null=True)
    precio = models.FloatField(null=True)
    costo = models.FloatField(null=True)

    