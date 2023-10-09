# Django
from django.contrib import admin

# Local
from .models import Client


class ClientAdmin(admin.ModelAdmin):
    """Admin panel for clients."""

    model = Client
    list_display = (
        'email',
        'first_name',
        'last_name',
        'username',
        'photo',
        'about',
        'is_active',
        'is_staff',
        'is_superuser',
        'date_joined',
    )
    search_fields = (
        'email',
        'first_name',
        'last_name',
        'username',
    )


admin.site.register(Client, ClientAdmin)

