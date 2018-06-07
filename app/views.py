from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
# from django.template.loader import get_template
# from django.template import Context
from . import models

# Create your views here.

def index(request):
    return render(request, 'index.html')

def visita(request):
    return redirect('visita.html')