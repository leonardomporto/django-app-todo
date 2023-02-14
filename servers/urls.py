
from django.urls import path
from .views import server_read, server_create, server_update, server_delete

urlpatterns = [
    path('server-create', server_create, name='server_create'),
    # path('server-read', server_read, name='server_read'),
    # path('server-update/<slug:slug>', server_update, name='server_update'),
    # path('server-delete/<slug:slug>', server_delete, name='server_delete'),
]
