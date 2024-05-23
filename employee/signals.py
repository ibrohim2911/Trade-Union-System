from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import datetime
from .models import Employee

from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from .models import Employee

@receiver(post_save, sender=Employee)
def calculate_point(sender, instance, created, **kwargs):
    # Check if the flag is set to prevent recursive save
    if hasattr(instance, '_signal_processing'):
        return
    print(instance.handicapped, type(instance.handicapped))
    # Set the flag to indicate the instance is being processed
    instance._signal_processing = True

    x = 0
    p = 0
    if instance.gender == 'Erkak':
        x = 1
    else:
        x = 1.3
    p = instance.age

 #   if instance.handicapped and int(instance.handicapped.level) == 2:
 #       p = p + 2
  #  elif instance.handicapped == "3":
  #      p = p + 3
    if instance.role == "3":
        p = p + 3
    elif instance.role == "4":
        p = p + 4
    if instance.illness == "3":
        p = p + 3
    if instance.family_status == "1":
        p = p + 1
    elif instance.family_status == "2":
        p = p + 2

    instance.points = p * x

    # Save the instance with the updated points
    instance.save(update_fields=['points'])

    # Print the points (for debugging purposes)
    print(instance.points)

    try:
        print(instance.organization)
    except:
        pass

    # Clean up the flag after saving
    del instance._signal_processing

    return instance
