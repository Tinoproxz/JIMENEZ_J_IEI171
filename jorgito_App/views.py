from django.shortcuts import render,redirect
from .forms import SociosForm
from .import forms
from .models import Socios

# Create your views here.
def index (request):
    return render (request,'index.html')

def listadoSocios(request):
    socios = Socios.objects.all()
    form = forms.SociosForm()

    if request.method == 'POST':
        form = SociosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/socios')

    data = {'socio': socios, 'formu': form}
    return render(request, 'all.html', data)

    
def eliminarSocio(request,id):
    socio = Socios.objects.get(id=id)
    socio.delete()
    return redirect('/socios')

def editarSocio(request, id):
    soc = Socios.objects.get(id=id)
    form = SociosForm(instance=soc)
    if request.method == 'POST':
        form = SociosForm(request.POST, instance=soc)
        if form.is_valid():
            form.save()
        else:
            data = {'formu': form}
            return render (request, 'edicion.html',data)
        return redirect('/socios')
    data = {'formu': form}
    return render(request,'edicion.html',data)