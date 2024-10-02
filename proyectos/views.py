from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from .models import Instrumento
from .forms import InstrumentoForm

def proyectos(request):
    instrumentos = Instrumento.objects.all()
    return render(request, 'proyectos/proyectos.html', {'instrumentos': instrumentos})


def lista_instrumentos(request):
    instrumentos = Instrumento.objects.all()
    return render(request, 'proyectos/proyectos.html', {'instrumentos': instrumentos})


def crear_instrumento(request):
    if request.method == 'POST':
        form = InstrumentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proyectos')  # Cambiar a 'proyectos' que es el nombre correcto en tu urls.py
    else:
        form = InstrumentoForm()
    return render(request, 'proyectos/crear_instrumento.html', {'form': form})

def editar_instrumento(request, instrumento_id):
    instrumento = get_object_or_404(Instrumento, id=instrumento_id)
    
    # Verifica si el estatus es 'Pendiente'
    if instrumento.estatus != 'Pendiente':
        return HttpResponseForbidden("No puedes editar un instrumento que ya ha iniciado su validación.")

    if request.method == 'POST':
        form = InstrumentoForm(request.POST, instance=instrumento)
        if form.is_valid():
            form.save()
            return redirect('proyectos')
    else:
        form = InstrumentoForm(instance=instrumento)
    
    return render(request, 'proyectos/editar_instrumento.html', {'form': form, 'instrumento': instrumento})

def eliminar_instrumento(request, instrumento_id):
    instrumento = get_object_or_404(Instrumento, id=instrumento_id)
    
    # Verifica si el estatus es 'Pendiente'
    if instrumento.estatus != 'Pendiente':
        return HttpResponseForbidden("No puedes eliminar un instrumento que ya ha iniciado su validación.")
    
    if request.method == 'POST':
        instrumento.delete()
        return redirect('proyectos')
    
    return render(request, 'proyectos/eliminar_instrumento.html', {'instrumento': instrumento})