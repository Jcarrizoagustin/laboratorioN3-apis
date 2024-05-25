import requests
from decimal import Decimal

DOLAR_API_BLUE_URL = 'https://dolarapi.com/v1/dolares/blue'

def get_usd_from_api():
    try:
        response = requests.get(DOLAR_API_BLUE_URL)
        datos = response.json()
        return Decimal(datos['venta'])
    except Exception as err:
        print(err)