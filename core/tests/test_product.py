import pytest
from .fixtures import api_client, crear_producto


def test_lista():
    assert list(reversed([1, 2, 3])) == [3, 2, 1]

@pytest.mark.django_db
def test_api_list_product(api_client, crear_producto):
    client = api_client
    response = client.get('/api/v1/productos/')
    
    #Compara el código 200
    assert response.status_code == 200
    product_json = response.json()
    
    #Comparo el nombre del producto (funciona)
    assert product_json[0]['nombre']=='test-prueba'
    
    #Comparo el nombre del producto (falla)
    #assert product_json[0]['nombre'] =='test-falla'
    
    #Comparo la cantidad de elementos
    assert len(product_json) == 1