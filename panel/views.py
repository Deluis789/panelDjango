from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def listar(request):
    return render(request, 'usuarios/listar.html', {})


def actualizar(request):
    return render(request, 'usuarios/actualizar.html', {})


def agregar(request):
    return render(request, 'usuarios/agregar.html', {})


def eliminar(request):
    return render(request, 'usuarios/eliminar.html', {})


