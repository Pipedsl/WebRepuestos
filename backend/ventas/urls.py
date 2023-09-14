from rest_framework import routers
from ventas.views import carritoView, ProductoViewSet, EmpleadoViewSet, ClienteViewSet, ProveedorViewSet, VentaViewSet, VentaProductoViewSet, UserViewSet, LogoutView , LoginView
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
router  = routers.DefaultRouter()
router.register('producto', ProductoViewSet)
router.register('empleado', EmpleadoViewSet)
router.register('cliente', ClienteViewSet)
router.register('proveedor', ProveedorViewSet)
router.register('venta', VentaViewSet)
router.register('ventaproducto',VentaProductoViewSet)
router.register('user', UserViewSet)

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('carrito/',carritoView),
    
] + router.urls

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)