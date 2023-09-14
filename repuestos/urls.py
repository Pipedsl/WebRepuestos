from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('empleado/', views.empleado, name='empleado'),
    path('cliente/', views.cliente, name='cliente'),
    path('proveedor/', views.proveedor, name='proveedor'),
    path('empleado_list/', views.empleado_list, name='empleado_list'),
    path('ingreso/', views.ingreso, name='ingreso'),
    path('recupera_contraseña/', views.recupera_contraseña, name='recupera_contraseña'),
    path('cliente_list/', views.cliente_list, name='cliente_list'),
    path('proveedor_list/', views.proveedor_list, name='proveedor_list'),
    path('contact', views.contact, name='contact'),
    path('sucursales', views.sucursales, name='sucursales'),
    path('carrito', views.carrito, name='carrito'),

]
