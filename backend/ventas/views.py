from rest_framework import viewsets, permissions
from django.shortcuts import redirect, render
from ventas.models import Carrito, ItemCarrito, Producto, Cliente, Empleado, Proveedor, Venta, VentaProducto
from ventas.serializers import ItemCarritoSerializer, ProductoSerializer, ClienteSerializer, EmpleadoSerializer, ProveedorSerializer, VentaSerializer, VentaProductoSerializer, UserSerializer
from rest_framework import status,views, response
from rest_framework import authentication
from django.contrib.auth.models import User
from django.contrib.auth import logout ,authenticate, login 
from rest_framework.authtoken.models import Token

# class JSONResponse(HttpResponse):
#     """
#     An HttpResponse that renders its content into JSON.
#     """
#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(content, **kwargs)

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [permissions.AllowAny]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # authentication_classes = [authentication.BasicAuthentication]
    

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()  
    permission_classes = [permissions.AllowAny]
    serializer_class = EmpleadoSerializer
    
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()  
    permission_classes = [permissions.AllowAny]
    serializer_class = ClienteSerializer
    
class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()  
    permission_classes = [permissions.AllowAny]
    serializer_class = ProveedorSerializer

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication,]
    serializer_class = VentaSerializer

class VentaProductoViewSet(viewsets.ModelViewSet):
    queryset = VentaProducto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = VentaProductoSerializer
    
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser,]
    authentication_classes = [authentication.BasicAuthentication,]

class LoginView(views.APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        # Recuperamos las credenciales y autenticamos al usuario
        username2= request.data.get('username', None)
        password2 = request.data.get('password', None)
        if username2 is None or password2 is None:
            return response.Response({'message': 'Please provide both username and password'},status=status.HTTP_400_BAD_REQUEST)
        user2 = authenticate(username=username2, password=password2)
        if not user2:
            return response.Response({'message': 'Usuario o Contraseña incorrecto !!!! '},status=status.HTTP_404_NOT_FOUND)

        token, _ = Token.objects.get_or_create(user=user2)
        # Si es correcto añadimos a la request la información de sesión
        if user2:
            # para loguearse una sola vez
            # login(request, user)
            return response.Response({'message':'usuario y contraseña correctos!!!!'},status=status.HTTP_200_OK)
            #return response.Response({'token': token.key}, status=status.HTTP_200_OK)

        # Si no es correcto devolvemos un error en la petición
        return response.Response(status=status.HTTP_404_NOT_FOUND)        

class LogoutView(views.APIView):
    authentication_classes = [authentication.TokenAuthentication]
    def post(self, request):        
        request.user.auth_token.delete()
        # Borramos de la request la información de sesión
        logout(request)
        # Devolvemos la respuesta al cliente
        return response.Response({'message':'Sessión Cerrada y Token Eliminado !!!!'},status=status.HTTP_200_OK)
    


def carritoView(request):
    productos = Producto.objects.all()
    vproductos = VentaProducto.objects.all()
    return render(request, "carrito.html", {"lproducto": productos,"vpro":vproductos })

from rest_framework.views import APIView
from rest_framework.response import Response

class AgregarProductoCarritoView(views.APIView):
    def post(self, request):
        # Obtiene el carrito actual del usuario
        carrito = Carrito.objects.get(id=request.user.carrito_id)
        
        # Obtiene el ID del producto a agregar
        producto_id = request.data.get('producto_id')
        producto = Producto.objects.get(id=producto_id)
        
        # Crea un nuevo elemento de carrito y lo asocia al carrito y al producto
        item_carrito = ItemCarrito(carrito=carrito, producto=producto, cantidad=1)
        item_carrito.save()
        
        return Response({'message': 'Producto agregado al carrito'})

class EliminarProductoCarritoView(views.APIView):
    def delete(self, request):
        # Obtiene el carrito actual del usuario
        carrito = Carrito.objects.get(id=request.user.carrito_id)
        
        # Obtiene el ID del producto a eliminar
        producto_id = request.data.get('producto_id')
        
        # Elimina el elemento de carrito asociado al producto
        item_carrito = ItemCarrito.objects.get(carrito=carrito, producto_id=producto_id)
        item_carrito.delete()
        
        return Response({'message': 'Producto eliminado del carrito'})