from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Client(models.Model):

    name = models.CharField(max_length=200, verbose_name='Nazwa')
    vat_number = models.CharField(max_length=13, verbose_name='NIP')
    contact_person = models.CharField(max_length=30, verbose_name='Osoba kontaktowa')
    phone_number = models.CharField(max_length=11, verbose_name='Numer telefonu')
    e_mail = models.EmailField(blank=True, verbose_name='Adres e-mail')
    comments = models.CharField(max_length=500, blank=True, verbose_name='Komentarz')
    vip = models.BooleanField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.name)

class Task(models.Model):

    TYPE = (
        ('SERWIS','SERWIS'),
        ('CZĘŚCI','CZĘŚCI'),
        ('MASZYNY','MASZYNY'),
    )

    STATUS = (
        ('NOWE', 'NOWE'),
        ('W TRAKCIE', 'W TRAKCIE'),
        ('ZAKOŃCZONE', 'ZAKOŃCZONE'),
    )
    type = models.CharField(max_length=100, choices=TYPE, verbose_name='Typ')
    name = models.CharField(max_length=200, verbose_name='Nazwa')
    date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.CharField(max_length=200, choices=STATUS, default='NOWE')
    comments = models.CharField(max_length=500, blank=True)
    success = models.BooleanField(null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.name)

class TaskProgress(models.Model):

    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)
    progress_information = models.TextField(max_length=500, verbose_name='Informacje')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.progress_information)

class PhoneCall(models.Model):

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    comment = models.TextField(max_length=1000, verbose_name='Przebieg rozmowy')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_next_call = models.DateTimeField(name="Planowana data kolejnej rozmowy", null=True)

    
    def __str__(self):
        return str(self.client)
