from django import forms
from django.forms.widgets import TextInput, Textarea
from .models import *

class blogForm(forms.ModelForm):
    class Meta:
        model = blog
        fields = '__all__'

class commentForm(forms.ModelForm):
    class Meta:
        model = commentSession
        fields = ['name','text']
        widgets = {
            'name' : TextInput(attrs={
                'class': 'grid grid-cols-1 rounded-lg w-full p-1 bg-white outline-none focus:border-blue-300',
                'placeholder': 'Nama Lengkap'
            }),
            'text' : Textarea(attrs={
                'class': 'grid grid-cols-1 rounded-lg border-2 focus:border-blue-300'
            })
        }
        