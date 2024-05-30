#product_stock_validator retorna True si hay
from .models import DetalleOrden

def existe_producto_en_orden_validator(orden, producto):
    items_orden = DetalleOrden.objects.filter(orden=orden)
    for item in items_orden:
        if item.producto == producto:
            return True
    return False

def validar_cantidad(cantidad):
    if cantidad is None or cantidad == '' or int(cantidad) <= 0:
        raise Exception(f'Cantidad no puede contener el valor {cantidad}')