from django.shortcuts import render, redirect
from mantenimiento.models import Cliente
from mantenimiento.forms import ClienteForm


def listarCliente(request):
    lista = Cliente.objects.all().order_by('pk')
    opciones = {'menu': 'Mantenimiento Cliente',
                'modulo': 'Clientes',
                'listado': lista}
    return render(request, 'cliente/listar_cliente.html', opciones)


def agregarCliente(request):
    opciones = {'menu': 'Mantenimiento Cliente',
                'modulo': 'Agregar Clientes',
                }

    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm()
        opciones['formulario'] = form
    return render(request, 'cliente/form_cliente.html', opciones)


def editarCliente(request, id):
    opciones = {'menu': 'Mantenimiento Cliente',
                'modulo': 'Editar Clientes',
                }
    buscar = Cliente.objects.get(id=id)
    if request.method == 'GET':
        form = ClienteForm(instance=buscar)
        opciones['formulario'] = form
    else:
        form = ClienteForm(request.POST, instance=buscar)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    return render(request, 'cliente/form_cliente.html', opciones)


def eliminarCliente(request, id):
    buscar = Cliente.objects.get(id=id)
    opciones = {'menu': 'Mantenimiento Cliente',
                'modulo': 'Eliminar Clientes',
                'registro': buscar
                }
    if request.method == 'POST':
        buscar.delete()
        return redirect('clientes')
    return render(request, 'cliente/elim_cliente.html', opciones)
