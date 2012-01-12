# -*- coding: utf-8 -*-
# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response
def index(request):
    return HttpResponse("malkovich malkovich malkovich malkovich malkovich malkovich")

def add(request):
    from .models import Servicio
    servicio = Servicio(name="cafeteria",description="Sirve refrescos", providerurl="http://vendo_espacio_publicidad.com")
    servicio.save()
    servicios = Servicio.objects.all()
    return render_to_response("add.html", { 'servicios':servicios})
