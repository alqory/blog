from django import forms
from django.db.models import fields
from .models import *

class blogForm(forms.ModelForm):
    class Meta:
        model = blog
        fields = '__all__'

class commentForm(forms.ModelForm):
    class Meta:
        model = commentSession
        fields = ['name','text']
        