#from rest_framework import routers
from rest_framework_nested import routers
from core import api


#Inicializar enrutamiento en DRF
router = routers.DefaultRouter()

#Registrar URL de ViewSet
router.register(prefix='productos', viewset=api.ProductoViewSet)
router.register(prefix='ordenes', viewset=api.OrdenViewSet)

#Utilizamos rest_framework_nested
detalle_router = routers.NestedDefaultRouter(router, r'ordenes', lookup='orden')
detalle_router.register(r'detalle', api.DetalleOrdenViewSet,basename='orden-detalle')

urlpatterns = router.urls + detalle_router.urls
