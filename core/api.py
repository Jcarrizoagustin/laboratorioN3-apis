from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import NotFound
from rest_framework.mixins import CreateModelMixin
from .serializers import ProductoSerializer, OrdenSerializer, DetalleOrdenSerializer
from .models import Producto, Orden, DetalleOrden
from .validators import existe_producto_en_orden_validator,validar_cantidad
from .services import disminuir_stock_producto,aumentar_stock_producto,aumentar_cantidad_en_detalle_orden

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
            aumentar_stock_producto(product,detalle.cantidad)
        return super().destroy(request, *args, **kwargs)


#Detalle Orden
class DetalleOrdenViewSet(viewsets.ModelViewSet,CreateModelMixin):

    serializer_class = DetalleOrdenSerializer

    def get_queryset(self):
        orden_id = self.kwargs['orden_pk']
        return DetalleOrden.objects.filter(orden=orden_id)

    def create(self, request, *args, **kwargs):
        cantidad = self.request.data.get('cantidad')
        orden_id = self.kwargs['orden_pk']
        producto_id = self.request.data.get('producto')

        try:
            validar_cantidad(cantidad)
        except Exception as e:
            return Response({'error':e.args[0]},status=status.HTTP_400_BAD_REQUEST)
            

        cantidad = int(cantidad)
        orden = get_object_or_404(Orden, pk=orden_id)
        producto = get_object_or_404(Producto, pk=producto_id)

        if (producto.stock >= cantidad):
            if existe_producto_en_orden_validator(orden, producto):
                detalle = DetalleOrden.objects.filter(orden = orden_id, producto = producto_id).first()
                aumentar_cantidad_en_detalle_orden(detalle,cantidad)
                disminuir_stock_producto(producto,cantidad)
                serializer = self.get_serializer(detalle)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                detalle = DetalleOrden(None,orden_id,cantidad,producto_id)
                detalle.save()
                disminuir_stock_producto(producto,cantidad)
                serializer = self.get_serializer(detalle)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error':'No tenemos suficiente stock.'}, status=status.HTTP_409_CONFLICT)

        
    
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            producto_id = instance.producto.id
            cantidad = int(instance.cantidad)
            producto = get_object_or_404(Producto, pk=producto_id)
            aumentar_stock_producto(producto,cantidad)
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except NotFound:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except AttributeError:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        
    def update(self, request, *args, **kwargs):
        try:
            cantidad = int(request.data.get('cantidad'))
            instance = self.get_object()
            producto = get_object_or_404(Producto,pk=instance.producto.id)
            diferencia_cantidad = instance.cantidad - cantidad
            if(diferencia_cantidad > 0):
                aumentar_stock_producto(producto,diferencia_cantidad)
            else:
                disminuir_stock_producto(producto,abs(diferencia_cantidad))
            instance.cantidad = cantidad
            instance.save()
            serializer = self.get_serializer(instance)
            return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'Error':'No hay sufuciente stock'},status=status.HTTP_409_CONFLICT)
        