from django import forms
from mantenimiento.models import Cliente, Producto


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre', 'ruc', 'direccion', 'producto')
        label = {'nombre': 'Nombres Completos', 'ruc': 'Ruc', 'direccion': 'Dirección', 'producto': 'Productos'}


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('descripcion', 'precio', 'stock', 'iva')
        label = {'descripcion': 'Descripción', 'precio': 'Precio', 'stock': 'Stock', 'iva': 'Iva'}
