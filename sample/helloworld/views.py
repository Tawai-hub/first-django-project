from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def index(request):
    name = "Eric Tawai"
    template = loader.get_template('index.html')
    context = {
        'name': name
    }
    return HttpResponse(template.render(context, request))