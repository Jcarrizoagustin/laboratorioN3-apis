from .fixtures import crear_producto_fixture, api_client
import pytest

# # TEST PRODUCTO
@pytest.mark.django_db
def test_recuperar_producto(api_client,crear_producto_fixture):
    
    producto = crear_producto_fixture
    client = api_client

    response = client.get(f'/api/v1/productos/{producto.id}/')
    assert response.json()['id'] == str(producto.id)
    assert response.json()['nombre'] == 'Camisa'
    assert response.json()['stock'] == 5
    assert response.status_code == 200
