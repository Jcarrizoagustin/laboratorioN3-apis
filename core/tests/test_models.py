import pytest

from core.models import DetalleOrden, Orden, Producto

@pytest.mark.django_db
def test_producto_creacion():
    producto = Producto.objects.create(nombre="Test", precio=100.0, stock=10)
    assert producto.nombre == "Test"
    assert producto.precio == 100.0
    assert producto.stock == 10

@pytest.mark.django_db
def test_orden_creacion():
    orden = Orden.objects.create()
    assert orden.fecha_hora is not None

@pytest.mark.django_db
def test_detalle_orden_creacion():
    producto = Producto.objects.create(nombre="Test", precio=100.0, stock=10)
    orden = Orden.objects.create()
    detalle = DetalleOrden.objects.create(orden=orden, producto=producto, cantidad=2)

    assert detalle.cantidad == 2
    assert detalle.producto == producto
    assert detalle.orden == orden
