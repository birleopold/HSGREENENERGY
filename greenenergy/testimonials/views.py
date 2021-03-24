from django.shortcuts import render
from django.views.generic import ListView
from .models import Testmony
from .forms import TestmonyForm
# Create your views here.

class Testmony_list(ListView):
    model = Testmony
    context_object_name = 'testmonies'


def testmony(request):
    if request.method == 'POST':
        form = TestmonyForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse('Thanks for your feedback')
          
    else:
        form = TestmonyForm()
    return render(request, 'testimonials/testmony_create.html', {'form': form})