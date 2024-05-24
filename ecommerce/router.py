from rest_framework import routers
from core import api
from rest_framework.documentation import include_docs_urls

#Inicializar enrutamiento en DRF
router = routers.DefaultRouter()

#Registrar URL de ViewSet

router.register(prefix='producto', viewset=api.ProductoViewSet)
router.register(prefix='orden', viewset=api.OrdenViewSet)
router. register(prefix='detalle_orden', viewset=api.DetalleOrdenViewSet)
# router. register(prefix='docs', include_docs_urls(title="Ecommerce API"))


urlpatterns = router.urls
