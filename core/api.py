from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import ProductoSerializer, OrdenSerializer, DetalleOrdenSerializer
from .models import Producto, Orden, DetalleOrden


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer



class OrdenViewSet(viewsets.ModelViewSet):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

    def destroy(self, request, *args, **kwargs):
        instance  = self.get_object()
        for detalle in instance.DetalleOrden.all():
            detalle.delete()
        return super().destroy(request, *args, **kwargs)



class DetalleOrdenViewSet(viewsets.ModelViewSet):
    queryset = DetalleOrden.objects.all()
    serializer_class = DetalleOrdenSerializer

    def create(self, request, *args, **kwargs):
        orden = request.data.get('orden')
        cantidad = request.data.get('cantidad')
        producto = request.data.get('producto')

        detalle = DetalleOrden.objects.filter(orden_id=orden, producto_id=producto).first()
        if detalle:
            detalle.cantidad += int(cantidad)
            detalle.save()
            return Response(status=status.HTTP_201_CREATED)

        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        cantidad = request.data.get('cantidad',instance.cantidad)

        if int(cantidad)<=0:
            return Response({'error':'La cantidad debe ser mayor a 0'}, status=status.HTTP_400_BAD_REQUEST)
        
        instance.cantidad = cantidad
        instance.save()
        
        return super().update(request, *args, **kwargs)