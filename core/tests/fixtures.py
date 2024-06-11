import pytest

from core.models import Producto, Orden, DetalleOrden

## API CLIENT ##

@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()

## PRODUCTOS ##

@pytest.fixture
def crear_producto_fixture():
    producto, _ = Producto.objects.get_or_create(
        nombre = 'Camisa',
        precio = 18000.00,
        stock = 5
    )
    return producto


@pytest.fixture
def crear_orden():
    orden, _ = Orden.objects.get_or_create(
        id=None,
        fecha_hora=None
    )
    return orden

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

## ORDENES - DETALLE ORDEN ##
@pytest.fixture
def crear_orden_con_detalle():
    orden = crear_orden()
    producto = crear_producto()
    
    detalle,_ = DetalleOrden.objects.get_or_create(
        orden = orden,
        producto = producto,
        cantidad = 2,
        precio = producto.precio
    )
    return detalle

@pytest.fixture
def crear_orden_con_detalles():
    orden = crear_orden()
    producto1, producto2 = crear_productos()

    detalles,_ = DetalleOrden.objects.get_or_create(
        orden = orden,
        cantidad = 2,
        producto = producto1,
        precio = producto1.precio

    )
    detalles2,_ = DetalleOrden.objects.get_or_create(
        orden = orden,
        cantidad = 3,
        producto = producto2,
        precio = producto2.precio
    )
    return [detalles,detalles2]

