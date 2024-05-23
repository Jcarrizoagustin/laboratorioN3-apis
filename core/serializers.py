from rest_framework import serializers
from .models import Producto, Orden, DetalleOrden

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id','nombre','precio','stock']

class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = ['id','fecha_hora']

class DetalleOrdenSerializer(serializers.ModelSerializer):
    orden = OrdenSerializer()
    producto = ProductoSerializer()
    class Meta:
        model = DetalleOrden
        fields = ['orden','cantidad','producto']