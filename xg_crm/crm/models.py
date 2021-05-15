from django.db import models

# Create your models here.

class Client(models.Model):

    name = models.CharField(max_length=200)
    vat_number = models.CharField(max_length=13)
    contact_person = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=11)
    comments = models.CharField(max_length=500, blank=True)
    vip = models.BooleanField(name='VIP')

    def __str__(self):
        return str(self.name)

class Task(models.Model):

    status_choices = (
        ('Nowe', 'Nowe'),
        ('W trakcie', 'W trakcie'),
        ('Zakonczone', 'Zakonczone'),
    )

    type_choices = (
        ('Serwis', 'Serwis'),
        ('Czesci', 'Czesci'),
        ('Maszyna', 'Maszyna'),
    )

    task_type = models.CharField(max_length=10, choices=type_choices)
    task_name = models.CharField(max_length=200)
    task_data = models.DateTimeField(auto_now_add=True)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.CharField(max_length=500, choices=status_choices)

    def __str__(self):
        return str(self.task_name)

class TaskProgress(models.Model):

    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    progress_information = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.progress_information)
