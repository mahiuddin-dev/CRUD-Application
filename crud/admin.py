from django.contrib import admin

from .models import Leads
# Register your models here.

class LeadsAdmin(admin.ModelAdmin):

    list_display = ['name', 'phone', 'email', 'designation']

admin.site.register(Leads, LeadsAdmin)