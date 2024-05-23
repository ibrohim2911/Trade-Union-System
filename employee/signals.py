from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Employee

@receiver(post_save, sender=Employee)
def calculate_point(sender, instance, created, *args, **kwargs):
    if created or not created:
        print(instance.full_name, type(instance.full_name))
        print(instance.job, type(instance.job))
        print(instance.phone_number, type(instance.phone_number))
        print(instance.gender, type(instance.gender))
        print(instance.user, type(instance.user))
        print(instance.age, type(instance.age))
        print(instance.salary, type(instance.salary))
        print(instance.passport, type(instance.passport))
        print(instance.taken_money, type(instance.taken_money))
        print(instance.used_money, type(instance.used_money))
        print(instance.hired_at, type(instance.hired_at))
        print(instance.work_starts_at, type(instance.work_starts_at))
        print(instance.work_ends_at, type(instance.work_ends_at))
        print(instance.handicapped, type(instance.handicapped))
        print(instance.role, type(instance.role))
        print(instance.illness, type(instance.illness))
        print(instance.family_status, type(instance.family_status))

        try:
            print(instance.organization)
        except:
            pass
