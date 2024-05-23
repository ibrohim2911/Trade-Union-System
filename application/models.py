from django.db import models
from utils.models import BaseModel
from utils.choices import AplicationStatusChoice
from employee.models import Employee



class Aplication(BaseModel):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=256)
    description = models.TextField()
    status = models.CharField(max_length=30, choices=AplicationStatusChoice.choices, default=AplicationStatusChoice.SEND)