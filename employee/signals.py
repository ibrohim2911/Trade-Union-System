from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Employee

@receiver(post_save, sender=Employee)
def calculate_point(sender, instance, created, *args, **kwargs):
    if created:
        pass