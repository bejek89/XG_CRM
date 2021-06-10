from .forms import *
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import *
from django.views.generic import ListView


class AllClientView(ListView):
    model = Client
    context_object_name = 'clients'

class AllTaskView(ListView):
    model = Task
    context_object_name = 'all_tasks'

def add_client(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'crm/client_form.html', context)


def client_details(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    phone_calls = client.phonecall_set.order_by('-date')
    tasks = client.task_set.order_by('-date')
    context = {'client': client, 'phone_calls':phone_calls, 'tasks': tasks}
    return render(request, 'crm/client_details.html', context)


def new_phone_call(request, client_id):
    client = Client.objects.get(id=client_id)
    if request.method != 'POST':
        form = PhoneCallForm()
    else:
        form = PhoneCallForm(data=request.POST)
        if form.is_valid():
            phone_call = form.save(commit=False)
            phone_call.client = client
            phone_call.save()
            return HttpResponseRedirect(reverse('crm:client_details', args=[client_id]))

    context = {'client': client, 'form': form}
    return render(request, 'crm/phone_call.html', context)


def new_task(request, client_id):
    client = Client.objects.get(id=client_id)
    if request.method != 'POST':
        form = TaskForm()
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.client = client
            task.save()
            return HttpResponseRedirect(reverse('crm:client_details', args=[client_id]))

    context = {'client': client, 'form': form}
    return render(request, 'crm/task_form.html', context)

def task_progres(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    progress = task.taskprogres_set.order_by('-date')
    context = {'task': task, 'progress': progress}
    return render(request, 'crm/task_progress.html', context)


# def client_details(request, client_id):
#     client = get_object_or_404(Client, id=client_id)
#     phone_calls = client.phonecall_set.order_by('-date')
#     tasks = client.task_set.order_by('-date')
#     context = {'client': client, 'phone_calls':phone_calls, 'tasks': tasks}
#     return render(request, 'crm/client_details.html', context)
