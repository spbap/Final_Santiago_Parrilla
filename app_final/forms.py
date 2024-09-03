from django import forms

class PersonaFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    edad = forms.IntegerField()
    email = forms.EmailField()
    
class ProductoFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)
    descripcion = forms.CharField()
    
class PedidoFormulario(forms.Form):
    persona = forms.CharField(max_length=100)
    producto = forms.CharField(max_length=100)
    fecha_pedido = forms.DateField()
    cantidad = forms.IntegerField()