from django.db import models
from django.utils import timezone
# Create your models here.

class Client(models.Model):

    name = models.CharField(max_length=200)
    vat_number = models.CharField(max_length=13)
    contact_person = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=11)
    e_mail = models.EmailField(blank=True)
    comments = models.CharField(max_length=500, blank=True)
    vip = models.BooleanField()

    def __str__(self):
        return str(self.name)

class TaskStatus(models.Model):

    status = models.CharField(max_length=20, null=True)

    def __str__(self):
        return str(self.status)

class TaskType(models.Model):

    type = models.CharField(max_length=20)

    def __str__(self):
        return str(self.type)

class Task(models.Model):

    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=200)
    task_data = models.DateTimeField(auto_now_add=True)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    task_status = models.ForeignKey(TaskStatus, on_delete=models.CASCADE, null=True)
    comments = models.CharField(max_length=500, blank=True)


    def __str__(self):
        return str(self.task_name)

class TaskProgress(models.Model):

    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    progress_information = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.progress_information)

class PhoneCall(models.Model):

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    comment = models.TextField(max_length=1000, name="Komentarz")
    date_next_call = models.DateTimeField(name="Planowana data kolejnej rozmowy", null=True)

    
    def __str__(self):
        return str(self.client)

class Machine(models.Model):

    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    MARK = (
        ('PONSSE', 'PONSSE'),
        ('JOHN_DEERE', 'JOHN DEERE'),
        ('KOMATSU', 'KOMATSU'),
        ('INNA', 'INNA'),
    )

    mark = models.CharField(
        max_length=10,
        choices=MARK,
    )

    model = models.CharField(
        max_length=20,
    )

