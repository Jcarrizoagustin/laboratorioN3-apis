

from core.models import Producto
import pytest


# Test para la validación de cantidad > 0
def test_validar_cantidad_mayor_cero():

    from core.validators import validar_cantidad
    
    with pytest.raises(Exception):
        validar_cantidad(-1)
    # No debería lanzar excepción
    validar_cantidad(1)
