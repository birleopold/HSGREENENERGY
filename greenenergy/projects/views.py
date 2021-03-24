from django.shortcuts import render
from django.views.generic import DetailView
from .models import Project

# Create your views here.


def project_list(request):

    projects = Project.objects.all()
    context = { 
        'projects': projects,
    }
    return render(request, 'projects/project_list.html', context )



class Project_detail(DetailView):
    model = Project
    context_object_name = 'project_detail'
    queryset = Project.objects.all()