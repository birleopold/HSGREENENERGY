from django import forms
from .models import Testmony

class TestmonyForm(forms.ModelForm):
    
    class Meta:
        model = Testmony
        fields = ("first_name", "last_name", "image1", "product", "message")