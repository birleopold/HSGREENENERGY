from django.shortcuts import render
from django.views.generic import ListView
from .models import Client

# Create your views here.


class Client_list(ListView):
    model = Client
    context_object_name = 'clients'
    template_name='home/index.html'



