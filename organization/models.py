from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from utils.models import BaseModel

class Organization(models.Model):
    
    organization_name = models.CharField(max_length=200)
    phone_number = PhoneNumberField(unique=True, region="UZ")
    money = models.PositiveBigIntegerField()
    monthly_money = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    users = models.ManyToManyField(User, related_name='user_organization')

    def __str__(self) -> str:
        return self.organization_name
    
class Event(BaseModel):
    name = models.CharField(max_length=256)
    participants = models.ManyToManyField(User, related_name='participated_event')
    spend_money = models.PositiveBigIntegerField(default=0)
    planning_time = models.DateTimeField()
    manager = models.ForeignKey(User, on_delete=models.CASCADE)