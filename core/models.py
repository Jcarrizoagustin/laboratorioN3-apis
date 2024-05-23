from django.db import models
import uuid

class Producto(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
          primary_key=True, editable=False)
    nombre = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits=9,decimal_places=2)
    stock = models.PositiveSmallIntegerField()

class Orden(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
          primary_key=True, editable=False)
    fecha_hora = models.DateTimeField(auto_now_add=True)

    def get_total(self):
        #ToDo implementar la funcion, punto 3 del laboratorio
        pass

    def get_total_usd(self):
        #ToDo implementar la funcion haciendo uso de la api https://dolarapi.com/v1/dolares/blue, punto 3 del laboratorio
        pass 

class DetalleOrden(models.Model):
    orden = models.ForeignKey(Orden,on_delete=models.CASCADE,blank=False)
    cantidad = models.PositiveSmallIntegerField()
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE,blank=False)