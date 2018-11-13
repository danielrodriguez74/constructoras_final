from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView 
from django.shortcuts import render 
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView 

from constructorasApp.models import Constructora, Edificio, Apartamento

# Create your views here.
def inicio(request):
    return render(request, 'base.html')

def constructoras_base(request):
    constructoras = Constructora.objects.all()
    context = {'constructoras_list': constructoras}
    return render(request, 'base.html', context)

def edificios_detail(request, id):
    edificios = Constructora.objects.get(id= id)
    context = {'object': edificios}
    return render(request, 'constructorasApp/edificios.html', context)

def apartamentos_detail(request, pk):
    apartamentos = Edificio.objects.get(id= pk)
    context = {'apartamentos': apartamentos}
    return render(request, 'constructorasApp/apartamentos.html', context)

def carrete_detail(request, pk):
    fotos = Apartamento.objects.get(id= pk)
    context = {'fotos': fotos}
    return render(request, 'constructorasApp/carreteFotos.html', context)

def ingreso(request):
    return render(request, 'constructorasApp/ingreso.html')

# --------------------------- CONSTRUCTORA ---------------------------------

class ConstructoraList(ListView):
    model = Constructora

class ConstructoraCreate(CreateView):
    model = Constructora
    fields = '__all__'
    success_url = reverse_lazy('constructora-list')

class ConstructoraUpdate(UpdateView):
    model = Constructora
    fields = '__all__'
    success_url = reverse_lazy('constructora-list')

class ConstructoraDetail(DetailView):
    model = Constructora

class ConstructoraDelete(DeleteView):
    model = Constructora
    success_url = reverse_lazy('constructora-list')


# --------------------------- EDIFICIO ---------------------------------

class EdificioList(ListView):
    model = Edificio

class EdificioCreate(CreateView):
    model = Edificio
    fields = '__all__'
    success_url = reverse_lazy('edificio-list')

class EdificioUpdate(UpdateView):
    model = Edificio
    fields = '__all__'
    success_url = reverse_lazy('edificio-list')

class EdificioDetail(DetailView):
    model = Edificio

class EdificioDelete(DeleteView):
    model = Edificio
    success_url = reverse_lazy('edificio-list')

def edificioListFilter(request, grado_id):
    grado = Grado.objects.filter(id=grado_id) 
    edificios = Edificio.objects.filter(grado=grado_id)
    context = {'edificios_data':edificios, 'grado_data':grado}
    return render(request, 'constructorasApp/edificio_filter_list.html', context)
    

# --------------------------- APARTAMENTO ---------------------------------

class ApartamentoList(ListView):
    model = Apartamento

class ApartamentoCreate(CreateView):
    model = Apartamento
    fields = '__all__'
    success_url = reverse_lazy('apartamentos-list')

class ApartamentoUpdate(UpdateView):
    model = Apartamento
    fields = '__all__'
    success_url = reverse_lazy('apartamentos-list')

class ApartamentoDetail(DetailView):
    model = Apartamento

class ApartamentoDelete(DeleteView):
    model = Apartamento
    success_url = reverse_lazy('apartamentos-list')

def apartamentoListFilter(request, grado_id):
    grado = Grado.objects.filter(id=grado_id) 
    Apartamentos = Apartamento.objects.filter(grado=grado_id)
    context = {'Apartamentos_data':Apartamentos, 'grado_data':grado}
    return render(request, 'constructorasApp/Apartamento_filter_list.html', context)
    