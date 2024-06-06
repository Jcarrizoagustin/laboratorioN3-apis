import pytest

from core.models import Producto, Orden, DetalleOrden

## API CLIENT ##

@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()

## PRODUCTOS ##

@pytest.fixture
def crear_producto():
    producto, _ = Producto.objects.get_or_create(
        nombre = 'Camisa',
        precio = 18000.00,
        stock = 5
    )
    return producto

@pytest.fixture
def crear_productos():
    producto, _ = Producto.objects.get_or_create(
        nombre = 'Remera',
        precio = 15.00,
        stock = 3
    )
    producto2, _ = Producto.objects.get_or_create(
        nombre = 'Jean',
        precio = 18.00,
        stock = 4
    )
    return [producto,producto2]

## ORDENES ##

@pytest.fixture
def crear_orden():
    orden, _ = Orden.objects.get_or_create(
        id=None,
        fecha_hora=None
    )
    return orden

## ORDENES - DETALLE ORDEN ##

'''@pytest.fixture(params=[True])
def crear_detalle_orden(orden_id, producto_id,cantidad):
    detalle_orden, _ = DetalleOrden.objects.get_or_create(
        orden = orden_id,
        cantidad = cantidad,
        producto = producto_id
    )
    return detalle_orden'''
