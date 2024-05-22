from django.contrib import admin
from .models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name')
    search_fields = ['name', "passport_id"]
admin.site.register(Employee, EmployeeAdmin)
