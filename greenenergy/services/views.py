from django.shortcuts import render
from django.views.generic import DetailView
from .models import Service

# Create your views here.




def service_list(request):
    services = Service.objects.all()
    context = {
        'services' : services
    }
    return render(request, 'services/service_list.html', context )



class Service_detail(DetailView):
    model = Service
    context_object_name = 'service_detail'
    queryset = Service.objects.all()