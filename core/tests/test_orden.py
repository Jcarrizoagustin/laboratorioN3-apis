from .fixtures import api_client,crear_producto,crear_productos,crear_orden #,crear_detalle_orden
from core.models import DetalleOrden
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