from django.db import models
from .services import get_usd_from_api
from decimal import Decimal, ROUND_HALF_UP
import uuid

class Producto(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)
    nombre = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits=9,decimal_places=2)
    stock = models.PositiveSmallIntegerField()

    def __str__(self):
        texto="{0} - ${1} - Cant. {2}"
        return texto.format(self.nombre, self.precio, self.stock)

class Orden(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    fecha_hora = models.DateTimeField(auto_now_add=True)

    def get_total(self):
        items = DetalleOrden.objects.filter(orden = self.id)
        total = 0
        for item in items:
            total += item.precio
        return total

    def get_total_usd(self):
        valor_usd_blue = get_usd_from_api()
        valor_orden = self.get_total()
        valor_en_usd = valor_orden/valor_usd_blue
        return valor_en_usd.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP) #Se devuelve el valor redondeado

    def __str__(self):
        return f'{self.id} - {self.fecha_hora}'

class DetalleOrden(models.Model):
    orden = models.ForeignKey(Orden,on_delete=models.CASCADE,blank=False)
    cantidad = models.PositiveSmallIntegerField()
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE,blank=False)
    precio = models.DecimalField(max_digits=9,decimal_places=2,null=True)

    def save(self, *args, **kwargs):
        self.precio = self.producto.precio * self.cantidad
        super().save(*args, **kwargs)
