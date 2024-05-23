from django.db import models


class GenderChoices(models.TextChoices):
    MALE = "Erkak", "Erkak"
    FAMELE = "Ayol", "Ayol"


class AplicationStatusChoice(models.TextChoices):
    SEND = "Yuborilgan", "Yuborilgan"
    READ = "O'qilgan", "O'qilgan"
    ACCEPTED = "Qabul qilingan", "Qabul qilingan"
    REJECTED = "Rad etilgan", "Rad etilgan"
class handicappedChoices(models.TextChoices):
    NOT = "0", "Nogiron emas"
    THIRD = "2", "3-guruh"
    SECOND = "3", "2-guruh"
class roleChoice(models.TextChoices):
    NOT = "0", "nazoratga olinmagan"
    IRON = "3", "temir daftar"
    WNC = "4", "ayollar va yoshlar daftari"
class illnessChoice(models.TextChoices):
    NOT = "0", "Sog'lom"
    HAS = "3", "muntazam kasalligi bor"
class familiyStatusChoice(models.TextChoices):
    NOT = "0", "Turmush qurmagan"
    READ = "1", "Turmush qurgan"
    ACCEPTED = "2", "Ajrashgan"
