from .fixtures import api_client,crear_producto,crear_productos,crear_orden #,crear_detalle_orden
from core.models import DetalleOrden, Orden, Producto
from django.urls import reverse
import pytest

API_BASE_URL= '/api/v1'

'''
Ejercicio N° 1 - 
    Verificar que al ejecutar el endpoint de recuperación de una orden, se devuelven los datos correctos de la orden y su detalle.
'''

@pytest.mark.django_db
def test_recuperar_orden(api_client,crear_orden):
    #Recupera la orden
    orden = crear_orden
    client = api_client

    response = client.get(f'/api/v1/ordenes/{orden.id}/')
    assert response.json()['id'] == str(orden.id)
    assert response.json()['total'] == 0.0
    assert response.status_code == 200

@pytest.mark.django_db
def test_recuperar_orden_detalle(api_client,crear_producto,crear_orden):
    orden = crear_orden
    client = api_client
    producto = crear_producto
    detalle_orden = DetalleOrden(None,orden.id,3,producto.id)
    detalle_orden.save()

    response = client.get(f'/api/v1/ordenes/{orden.id}/detalle/')

    assert response.status_code == 200
    assert response.json()[0]['cantidad'] == 3


# TEST PRODUCTO
@pytest.mark.django_db
def test_recuperar_producto(api_client,crear_producto):
    #Recupera la orden
    producto = crear_producto
    client = api_client

    response = client.get(f'/api/v1/productos/{producto.id}/')
    assert response.json()['id'] == str(producto.id)
    assert response.json()['nombre'] == 'Camisa'
    assert response.json()['stock'] == 5
    assert response.status_code == 200

'''
Ejercicio N° 2 - 
    Verificar que al ejecutar el endpoint de creación de un detalle de orden, ésta se cree
    correctamente, controlando que se haya actualizado el stock de producto relacionado.
'''


'''
Ejercicio N° 3 - 
    Verificar que al ejecutar el endpoint de creación de un detalle de orden, cuando se
    agrega un producto que ya está en otro detalle de la misma orden, se sume la cantidad
    de productos total para la orden y no existan dos registros de detalle orden con el
    mismo producto.
'''


'''
Ejercicio N° 4 - 
    Verificar que al ejecutar el endpoint de creación de un detalle orden, se produzca un
fallo al intentar procesar la cantidad de un producto que sea mayor al stock de ese
producto
'''

'''
Ejercicio N° 5 - 
    Verificar que al ejecutar el endpoint de eliminación de una orden, ésta se haya
    eliminado de la base de datos correctamente, junto con sus detalles, y que, además
    se haga incrementado el stock de producto relacionado con cada detalle de orden.
'''
@pytest.mark.django_db
def test_eliminar_orden(api_client, crear_orden, crear_producto):
    client = api_client
    orden = crear_orden
    producto = crear_producto

    stock_inicial = producto.stock

    #Creamos el detalle orden con los producto
    detalle_orden = DetalleOrden.objects.create(
            orden=orden,
            cantidad=3,
            producto=producto,
            precio = producto.precio
        )
    
    #Verificar que la orden existe en BD
    assert Orden.objects.filter(pk=orden.pk).exists()

    #Verificamos que el detalle exite en la BD
    assert DetalleOrden.objects.filter(orden=orden).exists()

    #Verificamos que el Stock se ha decrementado
    #producto.refresh_from_db()
    #stock_esperado = stock_inicial - detalle_orden.cantidad
    #assert producto.stock == stock_esperado
    
    #Forma 1 - Realizamos la solucitud DELETE
    response1 = client.delete(f'/api/v1/ordenes/{orden.pk}/')
    
    #Verificamos que la respuesta es "204 No content"
    assert response1.status_code == 204
    
    #Forma 2
    #Obtener URL para eliminar la orden
    #url = reverse('orden-detail',args=[orden.pk])
    
    #Realizamos la solucitud DELETE
    #response = client.delete(url, content_type='applications/json')
    
    #Verificamos que la respueta es "204 No Content"
    #assert response.status_code == 204
    
    #Verificar que la ORDEN se ha Eliminado
    assert not Orden.objects.filter(pk=orden.pk).exists()

    #Verificamos que los DETALLES de la ORDEN se han Eliminado
    assert not DetalleOrden.objects.filter(orden=orden).exists()

    #Verificar que el Stock del producto se ha Incrmentado
    producto.refresh_from_db()
    assert stock_inicial == 5





'''
Ejercicio N° 6 - 
    Verificar que el método get_total de una orden, devuelve el valor correcto de acuerdo
    al sub-total de cada detalle. 
'''

'''
Ejercicio N° 7 - 
    Verificar que el método get_total_usd de una orden, devuelve el valor correcto de
    acuerdo al total de la orden y la cotización del dólar blue (considerar “mockear” el valor
    del dólar blue, simulando la respuesta de la API externa). 
'''