from django.contrib import admin
from .models import Organization
# Register your models here.

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name')
    search_fields = ['name', "email"]
admin.site.register(Organization, OrganizationAdmin)
