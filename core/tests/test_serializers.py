from core.models import Orden, Producto
import pytest
from .fixtures import crear_producto_fixture, crear_orden_fixture


@pytest.mark.django_db
def test_producto_serializer(crear_producto_fixture):
    from core.serializers import ProductoSerializer

    producto = crear_producto_fixture

    serializer = ProductoSerializer(producto)
    data = serializer.data

    assert data['nombre'] == "Test"
    assert float(data['precio']) == 18000.00
    assert data['stock'] == 5

@pytest.mark.django_db
def test_orden_serializer(crear_orden_fixture):
    from core.serializers import OrdenSerializer
    
    orden = crear_orden_fixture

    serializer = OrdenSerializer(orden)
    data = serializer.data
    assert 'total' in data
    assert 'total_usd' in data