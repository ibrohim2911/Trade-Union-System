from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
#from employee.models import Employee
from django.db import models
# class Organization(AbstractUser):
#     name = m.CharField(max_length=200)
#     email = m.EmailField(unique=True)
#     money = m.IntegerField(default=0)
#     monthly_money = m.IntegerField(default=0)
#     #employees = m.ForeignKey(Employee, on_delete=m.CASCADE, related_name="employee_for_organization", null=True)
#     username = m.CharField(max_length=100, unique=True)
#     USERNAME_FIELD = "username"
#     REQUIRED_FIELDS = []  

#     def __str__(self):
#         return self.name

class Organization(models.Model):
    organization_staff = models.OneToOneField(User, on_delete=models.CASCADE)
    organization_name = models.CharField(max_length=200)
    total_money = models.IntegerField(default=0)
    spend_money = models.PositiveBigIntegerField(default=0)
    current_money = models.PositiveBigIntegerField(default=0)
    monthly_money = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.organization_name