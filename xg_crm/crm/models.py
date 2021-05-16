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

class TaskStatus(models.Model):

    status = models.CharField(max_length=20)

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
    task_status = models.ForeignKey(TaskStatus, on_delete=models.CASCADE)
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
    
    date = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=500)
    date_next_call = models.DateTimeField()
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.client_id)