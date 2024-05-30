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
    #orden = OrdenSerializer()
    #producto = ProductoSerializer()
    class Meta:
        model = DetalleOrden
        fields = '__all__'
        read_only_fields = ['orden','precio']

class OrdenSerializer(serializers.ModelSerializer):
    
    detalles = DetalleOrdenSerializer(many=True, read_only=True)
    total = serializers.SerializerMethodField()
    total_usd = serializers.SerializerMethodField()
    
    class Meta:
        model = Orden
        fields = ['id','fecha_hora','detalles','total','total_usd']
    
    def get_total(self, orden):
        return orden.get_total()
    
    def get_total_usd(self, orden):
        return orden.get_total_usd()