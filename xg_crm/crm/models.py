from django.db import models

# Create your models here.

class Client(models.Model):

    name = models.CharField(max_length=200, name='Nazwa')
    vat_number = models.IntegerField(max_length=10, name='NIP')
    contact_person = models.CharField(max_length=30, name='Osoba_kontatowa')
    phone_number = models.IntegerField(name='Numer_telefonu')

class Task(models.Model):

    status_choices = (
        ('Nowe', 'Nowe')
        ('W trakcie', 'W trakcie')
        ('Zakonczone', 'Zakonczone')
    )

    task_name = models.CharField(max_length=200, name='Zadanie')
    task_data = models.DateTimeField(auto_now_add=True)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.CharField(choices=status_choices)
    task_progress = models.TextField(name='Postep_zadania')