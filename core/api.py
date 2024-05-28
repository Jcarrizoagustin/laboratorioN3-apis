from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import NotFound
from rest_framework.mixins import CreateModelMixin
from .serializers import ProductoSerializer, OrdenSerializer, DetalleOrdenSerializer
from .models import Producto, Orden, DetalleOrden
from .validators import existe_producto_en_orden_validator

## Producto
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

#Ordenes
class OrdenViewSet(viewsets.ModelViewSet):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

    def destroy(self, request, *args, **kwargs):
        instance  = self.get_object()
        detalle_ordenes = DetalleOrden.objects.filter(orden=instance.id)
        for detalle in detalle_ordenes:
            #Reestablecemos el stock de los productos antes de eliminar una orden
            product = Producto.objects.filter(id=detalle.producto.id).first()
            product.stock += detalle.cantidad
            product.save()
        return super().destroy(request, *args, **kwargs)


#Detalle Orden
class DetalleOrdenViewSet(viewsets.ModelViewSet,CreateModelMixin):

    serializer_class = DetalleOrdenSerializer

    def get_queryset(self):
        orden_id = self.kwargs['orden_pk']
        return DetalleOrden.objects.filter(orden=orden_id)

    def perform_create(self, serializer):
        orden_id = self.kwargs['orden_pk']
        cantidad = int(self.request.data.get('cantidad'))
        producto_id = self.request.data.get('producto')

        orden = get_object_or_404(Orden, pk=orden_id)
        producto = get_object_or_404(Producto, pk=producto_id)

        if (producto.stock >= cantidad):
            if existe_producto_en_orden_validator(orden, producto):
                detalle = DetalleOrden.objects.filter(orden = orden_id, producto = producto_id).first()
                detalle.cantidad = int(cantidad)
                detalle.save()
                return Response(detalle,status = status.HTTP_200_OK)
            else:
                detalle = DetalleOrden(None,orden_id,cantidad,producto_id)
                detalle.save()
                producto.stock = producto.stock - cantidad
                producto.save()
                return Response(detalle)
        else:
            return Response({'error':'No tenemos suficiente stock.'}, status=status.HTTP_409_CONFLICT)

        
    
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            producto_id = instance.producto.id
            cantidad = int(instance.cantidad)
            producto = get_object_or_404(Producto, pk=producto_id)
            producto.stock = producto.stock + cantidad
            producto.save()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except NotFound:
            return Response(status=status.HTTP_404_NOT_FOUND)