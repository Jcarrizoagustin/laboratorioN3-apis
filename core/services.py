import requests
from decimal import Decimal
from django.conf import settings

API_URL = settings.DOLAR_BLUE_API_URL

def get_usd_from_api():
    try:
        response = requests.get(API_URL)
        datos = response.json()
        return Decimal(datos['venta'])
    except Exception as err:
        print(err)

def aumentar_stock_producto(producto, cantidad):
    producto.stock = producto.stock + cantidad
    producto.save()

def disminuir_stock_producto(producto, cantidad):
    producto.stock = producto.stock - cantidad
    producto.save()

def aumentar_cantidad_en_detalle_orden(detalle, cantidad):
    detalle.cantidad = detalle.cantidad + int(cantidad)
    detalle.save()