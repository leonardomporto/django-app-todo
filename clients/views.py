from django.shortcuts import render, redirect, get_object_or_404
from .models import Client
from .forms import ClientForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden



@login_required
def client_read(request):
    clients = Client.objects.all().filter(user=request.user)
    return render(request, 'clients/client-read.html', {'clients': clients})



@login_required
def client_create(request):
    form = ClientForm(request.POST or None)
    if form.is_valid():
        #onde era form.save() passou aser client.save() pra fazer uma pausar e adiconar o user logado na seção.
        client = form.save(commit=False)
        client.user = request.user
        client.save()
        return redirect('client_read')
    return render(request, 'clients/client-create.html', {'form': form})



@login_required
def client_update(request, slug):
    client = Client.objects.get(slug=slug)
    if client.user != request.user:
        return HttpResponseForbidden("Você não tem permissão para editar este cliente.")
        
    form = ClientForm(request.POST or None, instance=client)
    if form.is_valid():
        form.save()
        return redirect('client_read')
    return render(request, 'clients/client-create.html', {'form': form})



@login_required
def client_delete(request, slug):
    client = Client.objects.get(slug=slug)
    if request.method == 'POST':
        client.delete()
        return redirect('client_read')
    return render(request, 'clients/client_confirm_delete.html', {'client': client})
