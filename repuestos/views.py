from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def empleado(request):
    return render(request, 'empleado.html', {})

def cliente(request):
    return render(request, 'cliente.html', {})

def proveedor(request):
    return render(request, 'proveedor.html', {})

def empleado_list(request):
    return render(request, 'empleado_list.html', {})

def ingreso(request):
    return render(request, 'ingreso.html', {})

def recupera_contraseña(request):
    return render(request, 'recupera_contraseña.html', {})

def cliente_list(request):
    return render(request, 'cliente_list.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def sucursales(request):
    return render(request, 'sucursales.html', {})

def proveedor_list(request):
    return render(request, 'proveedor_list.html', {})

def carrito(request):
    return render(request, 'carrito.html', {})