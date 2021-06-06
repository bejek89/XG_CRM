from django import forms
from .models import *

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class PhoneCallForm(forms.ModelForm):
    class Meta:
        model = PhoneCall
        fields = [
            'Komentarz',
        ]

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'