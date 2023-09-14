from django.db import models
from datetime import datetime

class Producto(models.Model):
    productoName = models.CharField(max_length=200,)
    productoDescription = models.CharField(blank=True, max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    productoImage = models.ImageField(null=True, blank=True, upload_to='images/')
    # create_at = models.DateTimeField(default=datetime.datetime.now)
    def __str__ (self):
        return self.productoName

class Persona(models.Model):
    nombre = models.CharField('Nombre', max_length = 100)
    apellido = models.CharField('Apellido', max_length = 200, default='')
    foto = models.ImageField(null=True, blank=True, upload_to='fotos/')
    class Meta:
        abstract = True


class Empleado(Persona):
    rut = models.IntegerField(null=False, primary_key=True)
    dv = models.CharField(max_length=1, null=False)
    contacto = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    local = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return '{0},{1}'.format(self.apellido, self.nombre)
    
        
class Cliente(Persona):
    rut = models.IntegerField(null=False, primary_key=True)
    dv = models.CharField(max_length=1, null=False)
    contacto = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    local = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return '{0},{1}'.format(self.apellido,self.nombre)
    
        
class Proveedor(models.Model):
    rut = models.IntegerField(null=False, primary_key=True)
    dv = models.CharField(max_length=1, null=False)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    CATEGORIA_CHOICES = [
        ('accesorios', 'Accesorios'),
        ('carroceria', 'Carroceria'),
        ('motor', 'Motor')
    ]
    categoria = models.CharField(max_length=10, choices=CATEGORIA_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.nombre
    
class Venta(models.Model) :
    client = models.ForeignKey(Cliente,on_delete=models.CASCADE, verbose_name='Cliente ok', null=False)
    fecha = models.DateTimeField(default=datetime.now)
    description = models.TextField(blank = True)
    def __str__ (self):
        return '{0}'.format(self.id)

class VentaProducto(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, verbose_name='Nro Venta', null=False)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE, verbose_name='Producto', null=False)
    cantidad = models.PositiveIntegerField(default=0)
    preciounit = models.FloatField()
    modified = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    state = models.BooleanField(default = True)
    def __str__(self):
        return f'{self.venta} to {self.producto}'

    class Meta:
        indexes = [
                models.Index(fields=['venta', 'producto',]),
            ]

class Carrito(models.Model):
    productos = models.ManyToManyField(Producto, through='ItemCarrito')

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)  