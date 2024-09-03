from django.shortcuts import render
from .models import *
from app_final.forms import *
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'app_final/home.html')

def personas(request):
    return render(request, 'app_final/personas.html')

def productos(request):
    return render(request, 'app_final/productos.html')

def pedidos(request):
    return render(request, 'app_final/pedidos.html')

def sobre_mi(request):
    return render(request, 'app_final/sobre_mi.html')

@login_required
def nueva_persona(request):
    if request.method == 'POST':
        miformulario = PersonaFormulario(request.POST)
        if miformulario.is_valid():
            informacion = miformulario.cleaned_data
            persona = Persona(nombre=informacion['nombre'],apellido=informacion['apellido'],edad=informacion['edad'],email=informacion['email'])
            persona.save()
            return render(request, 'app_final/persona_ok.html')
        else:
            miformulario = PersonaFormulario()
    return render(request, 'app_final/nueva_persona.html')

@login_required
def nuevo_producto(request):
    if request.method == 'POST':
        miformulario = ProductoFormulario(request.POST)
        if miformulario.is_valid():
            informacion = miformulario.cleaned_data
            producto = Producto(nombre=informacion['nombre'],precio=informacion['precio'],descripcion=informacion['descripcion'])
            producto.save()
            return render(request, 'app_final/producto_ok.html')
        else:
            miformulario = ProductoFormulario()
    return render(request, 'app_final/nuevo_producto.html')

@login_required
def nuevo_pedido(request):
    if request.method == 'POST':
        miformulario = PedidoFormulario(request.POST)
        if miformulario.is_valid():
            informacion = miformulario.cleaned_data
            pedidos = Pedido(persona=informacion['persona'],producto=informacion['producto'],fecha_pedido=informacion['fecha_pedido'],cantidad=informacion['cantidad'])
            pedidos.save()
            return render(request, 'app_final/pedido_ok.html')
        else:
            miformulario = PedidoFormulario()
    return render(request, 'app_final/nuevo_pedido.html')

@login_required
def buscar_persona(request):
    return render(request, 'app_final/buscar_persona.html')

def search_persona(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        apellidos = Persona.objects.filter(nombre__icontains=nombre)
        edades = Persona.objects.filter(nombre__icontains=nombre)
        emails = Persona.objects.filter(nombre__icontains=nombre)
        
        return render(request,"app_final/search_persona.html",{"nombre":nombre,"apellidos":apellidos,"edades":edades,"emails":emails})
    else:
        return render(request,"app_final/search_persona.html")
 
# Buscar y actualizacion productos
@login_required
def buscar_producto(request):
    return render(request, 'app_final/buscar_producto.html')

def search_producto(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        precios = Producto.objects.filter(nombre__icontains=nombre)
        descripciones = Producto.objects.filter(nombre__icontains=nombre)
        
        return render(request,"app_final/search_producto.html",{"nombre":nombre,"precios":precios,"descripciones":descripciones})
    else:
        return render(request,"app_final/search_producto.html")
    
class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = "app_final/actualizar_producto.html"
    fields = ["nombre","precio","descripcion"]
    success_url = "/actualizacion_producto/"

def actualizacion_producto(request):
    return render(request, 'app_final/actualizacion_producto.html')

# Buscar y actualizacion productos
@login_required
def buscar_pedido(request):
    return render(request, 'app_final/buscar_pedido.html')

def search_pedido(request):
    if request.GET["producto"]:
        producto = request.GET["producto"]
        personas = Pedido.objects.filter(producto__icontains=producto)
        fecha_pedidos = Pedido.objects.filter(producto__icontains=producto)
        cantidades = Pedido.objects.filter(producto__icontains=producto)
        
        return render(request,"app_final/search_pedido.html",{"producto":producto,"personas":personas,"fecha_pedidos":fecha_pedidos,"cantidades":cantidades})
    else:
        return render(request,"app_final/search_pedido.html")
    
class PedidoUpdateView(UpdateView):
    model = Pedido
    template_name = "app_final/actualizar_pedido.html"
    fields = ["persona","producto","fecha_pedido","cantidad"]
    success_url = "/actualizacion_pedido/"
    
def actualizacion_pedido(request):
    return render(request, 'app_final/actualizacion_pedido.html')