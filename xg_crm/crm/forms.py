from django import forms
from .models import *

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'name',
            'vat_number',
            'contact_person',
            'phone_number',
            'e_mail',
            'comments',
            'vip',
       ]

class PhoneCallForm(forms.ModelForm):
    class Meta:
        model = PhoneCall
        fields = [
            'comment',
        ]

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'type',
            'name',
            'name',
            'comments',
        ]

class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = TaskProgress
        fields = [
            'progress_information',
        ]

class UpdateTaskStatus(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'status',
            'success',
        ]