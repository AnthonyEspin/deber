from django.shortcuts import render, redirect
from.models import Historial

from django.contrib import messages
# Create your views here.
# importando el modelo cargo
from .models import Historial



def inicio(request):
    listadoCargo=Historial.objects.all()
    
    return render(request, "inicio.html", {'cargos': listadoCargo})

def nuevoCargo (request):
    return render (request, "nuevoCargo.html")

#almacenando los datos de cargo en la bdd
def guardarCargo(request):
    usuario=request.POST["usuario"]
    actividad=request.POST["actividad"]
    fecha=request.POST["fecha"]
    resultado=request.POST["resultado"]
    nuevoCargo=Historial.objects.create(usuario=usuario, actividad=actividad, fecha=fecha, resultado=resultado )
    #Menaje de confirmacion
    messages.success(request,"Cargo guardado Existosamente")
    return redirect('/')


def eliminarCargo(request,id):
    cargoEliminar=Historial.objects.get(id=id)
    cargoEliminar.delete ()
    
    return redirect('/')


def editarCargo(request,id):
    cargoEditar=Historial.objects.get(id=id)
    return render(request,"editarCargo.html", {'cargoEditar':cargoEditar})


#CTUALIZANDO CARGOS 
def procesarEdicionCargo(request,id):
   
    usuario=request.POST["usuario"]
    actividad=request.POST["actividad"]
    fecha=request.POST["fecha"]
    resultado=request.POST["resultado"]
    cargo=Historial.objects.get(id=id)#buscando el cargo a editar por ID
    cargo.usuario=usuario
    cargo.actividad=actividad
    cargo.fecha=fecha
    cargo.resultado=resultado
    cargo.save()
    #mensaje de confirmacion
    messages.success(request,"Cargo actualizado Existosamente")
    return redirect('/')
