import requests
from decimal import Decimal
from django.conf import settings

API_URL = settings.DOLAR_BLUE_API_URL

def get_usd_from_api():
    try:
        response = requests.get(API_URL)
        datos = response.json()
        return Decimal(datos['venta'])
    except Exception as err:
        print(err)