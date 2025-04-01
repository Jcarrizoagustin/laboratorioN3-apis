
from core.models import Producto
import pytest

# Test para el servicio que actualiza el stock
@pytest.mark.django_db
def test_actualizar_stock_producto():
    from core.services import aumentar_stock_producto, disminuir_stock_producto
    
    producto = Producto.objects.create(nombre="Test", precio=100.0, stock=10)
    
    aumentar_stock_producto(producto, 10)
    
    producto.refresh_from_db()
    assert producto.stock == 20
    
    disminuir_stock_producto(producto, 10)
    
    producto.refresh_from_db()
    assert producto.stock == 10

