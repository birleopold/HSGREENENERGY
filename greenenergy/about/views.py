from django.shortcuts import render


from clients.models import Client
from testimonials.models import Testmony
from team.models import Team

# Create your views here.

def about(request):
    clients = Client.objects.all()
    testimonies = Testmony.objects.all()
    team = Team.objects.all()
    context = {
        'clients' : clients, 'testimonies': testimonies, 'team' : team

    }
    return render(request, 'home/about.html', context)


