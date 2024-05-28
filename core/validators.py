#product_stock_validator retorna True si hay
from .models import DetalleOrden

def existe_producto_en_orden_validator(orden, producto):
    items_orden = DetalleOrden.objects.filter(orden=orden)
    for item in items_orden:
        if item.producto == producto:
            return True
    return False