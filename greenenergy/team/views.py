from django.shortcuts import render
from django.views.generic import ListView

from .models import Team

# Create your views here.



class Team_list(ListView):
    model = Team
    context_object_name = 'team'

def team_list(request):
    team = Team.objects.all()
    context = {
        'team' : team
    }
    return render(request, 'team/team_list.html', context)