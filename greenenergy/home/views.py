from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import ContactForm
from django.http import HttpResponse
from projects.models import Project
from clients.models import Client
from services.models import Service

# Create your views here.


def home(request):
    services = Service.objects.all()
    projects = Project.objects.all()
    clients = Client.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()         
    else:
        form = ContactForm()


    context = {'form': form, 'services': services, 'projects': projects, 'clients': clients, }
    return render(request, 'home/index.html', context)



# class Home(TemplateView):
#     template_name='home/index.html'  

#     def post(self, request, *args, **kwargs):
#         context = self.get_context_data()
#         if context["form"].is_valid():
#             context['form'].save()
            
#         return super(TemplateView, self).render_to_response(context)

#     def get_context_data(self, **kwargs):        
#         context = super(Home, self).get_context_data(**kwargs)
#         form = ContactForm(self.request.POST or None)  # instance= 
#         context["form"] = form
#         context['clients'] = Client.objects.all()
#         context['projects'] = Project.objects.all()
#         context['services'] = Service.objects.all()
#         return context         

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse('Thanks for your feedback')
          
    else:
        form = ContactForm()
    return render(request, 'home/contact.html', {'form': form})






