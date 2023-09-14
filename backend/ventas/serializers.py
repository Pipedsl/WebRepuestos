from rest_framework import serializers
from ventas.models import ItemCarrito,Producto, Empleado, Cliente, Proveedor, Venta, VentaProducto, Persona
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
        read_only_fields = ['created_at']

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'
        extra_kwargs = {
            'fecha': {'read_only': True, 'required': False},
            # 'fecha' : {'read_only': True},
        }

class VentaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VentaProducto
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'groups', 'email']
        #esconder password
        extra_kwargs = {
            'password': {'write_only': True, 'required': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'precio']

class ItemCarritoSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer()
    
    class Meta:
        model = ItemCarrito
        fields = ['id', 'producto', 'cantidad']