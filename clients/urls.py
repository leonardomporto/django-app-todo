
from django.urls import path
from .views import client_read, client_create, client_update, client_delete

urlpatterns = [
    path('client-create', client_create, name='client_create'),
    path('client-read', client_read, name='client_read'),
    path('client-update/<slug:slug>', client_update, name='client_update'),
    path('client-delete/<slug:slug>', client_delete, name='client_delete'),
]
