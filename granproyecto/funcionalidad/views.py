# -*- coding: utf-8 -*-
# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.forms import ModelForm
from funcionalidad.models import Servicio


class Serviceform(ModelForm):
    class Meta:
        model = Servicio

def index(request):
    return HttpResponse("malkovich malkovich malkovich malkovich malkovich malkovich")

def add(request):
    servicio = Servicio(name="cafeteria",description="Sirve refrescos", providerurl="http://vendo_espacio_publicidad.com")
    servicio.save()
    servicios = Servicio.objects.all()
    return render_to_response("add.html", { 'servicios':servicios})

def add2(request):
    form = Serviceform(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            new_service = form.save()
            return redirect("/")
    return render_to_response('newadd.html', {'form':form}, context_instance = RequestContext(request))

