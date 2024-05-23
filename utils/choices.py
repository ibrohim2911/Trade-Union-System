from django.db import models


class GenderChoices(models.TextChoices):
    MALE = "Erkak", "Erkak"
    FAMELE = "Ayol", "Ayol"


class AplicationStatusChoice(models.TextChoices):
    SEND = "Yuborilgan", "Yuborilgan"
    READ = "O'qilgan", "O'qilgan"
    ACCEPTED = "Qabul qilingan", "Qabul qilingan"
    REJECTED = "Rad etilgan", "Rad etilgan"
