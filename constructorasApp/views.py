from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView 
from django.shortcuts import render 
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView 

from constructorasApp.models import Constructora, Edificio, Apartamento

#Autenticación
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

#Rest Framework
from rest_framework import viewsets
from .serializers import ConstructoraSerializer, EdificioSerializer, ApartamentoSerializer

# Create your views here.
def inicio(request):
    return render(request, 'base.html')

def constructoras_base(request):
    constructoras = Constructora.objects.all()
    context = {'constructoras_list': constructoras}
    return render(request, 'base.html', context)

def edificios_detail(request, id):
    edificios = Edificio.objects.filter(constructora=id)
    context = {'objects': edificios}
    return render(request, 'constructorasApp/edificios.html', context)

def apartamentos_detail(request, pk):
    apartamentos = Apartamento.objects.filter(edificio=pk)
    context = {'apartamentos': apartamentos}
    return render(request, 'constructorasApp/apartamentos.html', context)

def carrete_detail(request, pk):
    fotos = Apartamento.objects.get(id= pk)
    context = {'fotos': fotos}
    return render(request, 'constructorasApp/carreteFotos.html', context)

@login_required
def ingreso(request):
    return render(request, 'constructorasApp/ingreso.html')

# --------------------------- CONSTRUCTORA ---------------------------------
class ConstructoraList(ListView):
    model = Constructora

@method_decorator(login_required, name='dispatch')
class ConstructoraCreate(CreateView):
    model = Constructora
    fields = '__all__'
    success_url = reverse_lazy('constructoras-lista')

@method_decorator(login_required, name='dispatch')
class ConstructoraUpdate(UpdateView):
    model = Constructora
    fields = '__all__'
    success_url = reverse_lazy('constructoras-lista')

class ConstructoraDetail(DetailView):
    model = Constructora

@method_decorator(login_required, name='dispatch')
class ConstructoraDelete(DeleteView):
    model = Constructora
    success_url = reverse_lazy('constructoras-lista')


# --------------------------- EDIFICIO ---------------------------------

class EdificioList(ListView):
    model = Edificio

@method_decorator(login_required, name='dispatch')
class EdificioCreate(CreateView):
    model = Edificio
    fields = '__all__'
    success_url = reverse_lazy('edificios-lista')

@method_decorator(login_required, name='dispatch')
class EdificioUpdate(UpdateView):
    model = Edificio
    fields = '__all__'
    success_url = reverse_lazy('edificios-lista')

class EdificioDetail(DetailView):
    model = Edificio

@method_decorator(login_required, name='dispatch')
class EdificioDelete(DeleteView):
    model = Edificio
    success_url = reverse_lazy('edificios-lista')

def edificioListFilter(request, constructora_id):
    constructora = Constructora.objects.filter(id=constructora_id) 
    edificios = Edificio.objects.filter(constructora=constructora_id)
    context = {'edificios_data':edificios, 'constructora_data':constructora}
    return render(request, 'constructorasApp/edificio_filter_list.html', context)
    

# --------------------------- APARTAMENTO ---------------------------------

class ApartamentoList(ListView):
    model = Apartamento

@method_decorator(login_required, name='dispatch')
class ApartamentoCreate(CreateView):
    model = Apartamento
    fields = '__all__'
    success_url = reverse_lazy('apartamentos-lista')

@method_decorator(login_required, name='dispatch')
class ApartamentoUpdate(UpdateView):
    model = Apartamento
    fields = '__all__'
    success_url = reverse_lazy('apartamentos-lista')

class ApartamentoDetail(DetailView):
    model = Apartamento

@method_decorator(login_required, name='dispatch')
class ApartamentoDelete(DeleteView):
    model = Apartamento
    success_url = reverse_lazy('apartamentos-lista')

def apartamentoListFilter(request, edificio_id):
    edificio = Edificio.objects.filter(id=edificio_id) 
    apartamentos = Apartamento.objects.filter(edificio=edificio_id)
    context = {'apartamentos_data':apartamentos, 'edificio_data':edificio}
    return render(request, 'constructorasApp/Apartamento_filter_list.html', context)

# --------------------------- Serializers ---------------------------------

class ConstructoraViewSet(viewsets.ModelViewSet):
    queryset = Constructora.objects.all()
    serializer_class = ConstructoraSerializer

class EdificioViewSet(viewsets.ModelViewSet):
    queryset = Edificio.objects.all()
    serializer_class = EdificioSerializer

class ApartamentoViewSet(viewsets.ModelViewSet):
    queryset = Apartamento.objects.all()
    serializer_class = ApartamentoSerializer
    