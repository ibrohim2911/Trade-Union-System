from django.contrib import admin
from .models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name']
    search_fields = ['first_name', "passport_id"]
admin.site.register(Employee, EmployeeAdmin)
