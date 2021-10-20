from django import forms
from .models import *

class blogForm(forms.ModelForm):
    class Meta:
        model = blog
        fields = '__all__'