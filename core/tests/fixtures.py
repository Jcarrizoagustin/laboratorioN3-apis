import pytest
from core.models import Producto, Orden, DetalleOrden


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


## Product 
@pytest.fixture
def crear_producto():
    producto, _ = Producto.objects.get_or_create(
        nombre='test-prueba', 
        precio=10.50, 
        stock=10
        )
    return producto