from django.db import models

class handicappedChoice(models.TextChoices):
    zero = "0", "Nogiron emas"
    second = "3", "2-darajali"
    third = "2", "3-darajali"

class genderChoice(models.TextChoices):
    male = "1", "Erkak"
    female = "1.3", "Ayol"
