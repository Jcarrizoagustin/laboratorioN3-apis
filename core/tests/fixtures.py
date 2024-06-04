import pytest
from ..models import Producto, Orden, DetalleOrden

# @pytest.fixture
# def api_client():
#     from rest_framework import APIClient
#     return APIClient()


# ## Product 
# def create_product():
#     producto, creado = Producto.objects.get_or_create(nombre = 'galleta', precio=10.50, stock=10)
#     return producto