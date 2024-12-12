from multiprocessing.connection import Client

from django.contrib import admin

# from .forms import Client
from .models import Client
# Register your models here.
# admin.site.register(Client, ClientAdmin)

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'email', 'message')
    # search_fields = ('name', 'email', 'number')
    # list_filter = ['created_at']


admin.site.register(Client, ClientAdmin)