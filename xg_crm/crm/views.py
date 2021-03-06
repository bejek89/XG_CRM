from .forms import *
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import *
from django.views.generic import ListView


class AllClientView(ListView):
    model = Client
    context_object_name = 'clients'
    ordering = ['-date']

class AllTaskView(ListView):
    model = Task
    context_object_name = 'all_tasks'
    ordering = ['-date']

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


def new_tasks_list(request):
    new_task_list = Task.objects.filter(status='NOWE').order_by('-date')
    context = {'new_task_list': new_task_list}
    return render(request, 'crm/new_tasks_list.html', context)

def tasks_list_in_progress(request):
    task_list = Task.objects.filter(status='W TRAKCIE').order_by('-date')
    context = {'task_list': task_list}
    return render(request, 'crm/tasks_list_in_progress.html', context)

def ended_tasks_list(request):
    ended_task_list = Task.objects.filter(status='ZAKO??CZONE').order_by('-date')
    context = {'ended_task_list': ended_task_list}
    return render(request, 'crm/ended_tasks_list.html', context)

def update_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method != 'POST':
        form = UpdateTaskStatus()
    else:
        form = UpdateTaskStatus(instance=task, data=request.POST)
        if form.is_valid():
            update_task_status = form.save(commit=False)
            update_task_status.task = task
            form.save()
            return HttpResponseRedirect(reverse('crm:task_progress', args=[task.id]))

    context = {'task': task, 'form': form}
    return render(request, 'crm/edit_task_status.html', context)

def task_progress(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    progress = task.taskprogress_set.order_by('-date')

    if request.method != 'POST':
        form = UpdateTaskForm()
    else:
        form = UpdateTaskForm(data=request.POST)
        if form.is_valid():
            task_progress = form.save(commit=False)
            task_progress.task = task
            form.save()
            return HttpResponseRedirect(reverse('crm:task_progress', args=[task.id]))

    context = {'task': task, 'progress': progress, 'form': form}
    return render(request, 'crm/task_progress.html', context)