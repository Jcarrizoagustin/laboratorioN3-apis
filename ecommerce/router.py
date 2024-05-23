from rest_framework import routers
from core import api


#Inicializar enrutamiento en DRF
router = routers.DefaultRouter()

#Registrar URL de ViewSet

router.register(prefix='producto', viewset=api.ProductoViewSet)
router.register(prefix='orden', viewset=api.OrdenViewSet)
router. register(prefix='detalle_orden', viewset=api.DetalleOrdenViewSet)

urlpatterns = router.urls
