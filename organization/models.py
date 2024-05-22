from django.contrib.auth.models import AbstractUser
#from employee.models import Employee
from django.db import models as m
class Organization(AbstractUser):
    name = m.CharField(max_length=200)
    email = m.EmailField(unique=True)
    money = m.IntegerField(default=0)
    monthly_money = m.IntegerField(default=0)
    #employees = m.ForeignKey(Employee, on_delete=m.CASCADE, related_name="employee_for_organization", null=True)
    username = m.CharField(max_length=100, unique=True)
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []  

    def __str__(self):
        return self.name
    