from django.contrib.auth.models import AbstractUser
from employee.models import Employee
from django.db import models as m
class Organization(AbstractUser):
    name = m.CharField(max_length=200)
    email = m.EmailField(unique=True)
    money = m.IntegerField()
    monthly_money = m.IntegerField()
    employees = m.ForeignKey(Employee, on_delete=m.CASCADE, related_name="employee_for_organization")
      
    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = []  

    def __str__(self):
        return self.name
    