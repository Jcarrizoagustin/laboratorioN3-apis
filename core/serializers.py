from rest_framework import serializers
from .models import Producto, Orden, DetalleOrden



class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id','nombre','precio','stock']
    
    def validate_precio(self,precio):
        if precio < 0:
            raise serializers.ValidationError("El precio debe ser mayor que 0.")
        return precio

class DetalleOrdenSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    class Meta:
        model = DetalleOrden
        fields = ['id','cantidad','precio','product','producto']
        read_only_fields = ['orden','precio','product']
        extra_kwargs = {'producto': {'write_only': True}}
    
    def get_product(self,detalle):
        return ProductoSerializer(detalle.producto).data

class OrdenSerializer(serializers.ModelSerializer):
    
    detalles = DetalleOrdenSerializer(many=True, read_only=True)
    total = serializers.SerializerMethodField()
    total_usd = serializers.SerializerMethodField()
    fecha_hora = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S",read_only=True)
    
    class Meta:
        model = Orden
        fields = ['id','fecha_hora','detalles','total','total_usd']
    
    def get_total(self, orden):
        return orden.get_total()
    
    def get_total_usd(self, orden):
        return orden.get_total_usd()