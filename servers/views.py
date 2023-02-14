from django.shortcuts import render, redirect, get_object_or_404
from .models import Server
from .forms import ServerForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden



@login_required
def server_read(request):
    servers = Server.objects.all().filter(user=request.user)
    return render(request, 'servers/server-read.html', {'servers': servers})