from django.shortcuts import render, redirect
from crm.models import *
from crm.forms import *
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .forms import *

class AllClientView(ListView):
    model = Client
    context_object_name = 'clients'

def add_client(request):
	form = ClientForm()
	if request.method == 'POST':
		form = ClientForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context =  {'form':form}
	return render(request, 'crm/client_form.html', context)

def client_details(request, client_id):
    client = Client.objects.get(id=client_id)
    context = {'client': client}
    return render(request, 'crm/client_details.html', context)

def phone_call(request, client_id):
	client = Client.objects.get(id=client_id)
	if request.method != 'POST':
		form = PhoneCallForm()
	else:
		form = PhoneCallForm(data=request.POST)
		if form.is_valid():
			call = form.save(commit=False)
			call.client = client
			form.save()
			return redirect('/')
	context =  {'client':client, 'form':form}
	return render(request, 'crm/phone_call.html', context)

def new_task(request):
	action = 'create'
	form = PhoneCallForm()
	if request.method == 'POST':
		form = PhoneCallForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'action': action, 'form': form}
	return render(request, 'crm/phone_call.html', context)