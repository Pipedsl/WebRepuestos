from django.contrib import admin
from ventas.models import Producto, Empleado, Cliente, Proveedor, Venta, VentaProducto
from ventas.views import Carrito

admin.site.register(Producto)
admin.site.register(Empleado)
admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Venta)
admin.site.register(VentaProducto)
admin.site.register([Carrito])



