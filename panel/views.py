from django.shortcuts import redirect, render
from .models import Usuarios
# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def listar(request):
    users = Usuarios.objects.all()
    context = {'usuarios': users}
    return render(request, 'usuarios/listar.html', context)


def actualizar(request):
    if request.method == 'POST':
            #Agrego los datos
        if  request.POST.get('id') and request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('fecha_nac'):
            user_id_old = request.POST.get('id')
            user_old = Usuarios()
            user_old = Usuarios.objects.get(id = user_id_old)
            
            user = Usuarios()
            user.id = request.POST.get('id')
            user.nombre = request.POST.get('nombre')
            user.apellido = request.POST.get('apellido')
            user.correo = request.POST.get('correo')
            user.telefono = request.POST.get('telefono')
            user.f_nac = request.POST.get('fecha_nac')
            user.f_registro = user_old.f_registro
            user.save()
            return redirect('listar')
    else:
        users = Usuarios.objects.all()
        context = {'usuarios': users}
        return render(request, 'usuarios/actualizar.html', context)


def agregar(request):
    if request.method == 'POST':
        #Agrego los datos
        if request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('fecha_nac'):
            user = Usuarios()
            user.nombre = request.POST.get('nombre')
            user.apellido = request.POST.get('apellido')
            user.correo = request.POST.get('correo')
            user.telefono = request.POST.get('telefono')
            user.f_nac = request.POST.get('fecha_nac')
            user.save()
            return redirect('listar')
    else:
        return render(request, 'usuarios/agregar.html', {})


def eliminar(request):
    if request.method == 'POST':
        if request.POST.get('id'):
            id_borrar = request.POST.get('id')
            tupla = Usuarios.objects.get(id = id_borrar)
            tupla.delete()
            return redirect('listar')
    else:
        users = Usuarios.objects.all()
        context = {'usuarios': users}
    return render(request, 'usuarios/eliminar.html', context)


