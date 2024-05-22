from django.db import models as m
from organization.models import Organization
# Create your models here.

class Role(m.Model):
    in_role = m.CharField(max_length=100)
    proof = m.ImageField()

class GenderChoices(m.TextChoices):
    Erkak = "E", "Erkak"
    Ayol = "A", "Ayol"

class Family_status(m.Model):
    status = m.CharField(max_length=100)
    proof = m.ImageField()

class Handicapped(m.Model):
    how_handicapped = m.CharField(max_length=100)
    proof=m.ImageField()

class Illness(m.Model):
    how_ill = m.CharField(max_length=100)
    proof = m.ImageField()

class underageimg(m.Model):
    img = m.ImageField()

class Underages(m.Model):
    quantity = m.IntegerField()
    proof = m.ManyToManyField(underageimg, related_name="underageimgs")


class Employee(m.Model):    #xodim uchun class/model yaratildi va malumotlari olindi
    fio = m.CharField(max_length=300)
    phone_number = m.BigIntegerField(unique=True)
    age = m.DateField()
    gender=m.CharField(max_length=1, choices=GenderChoices.choices, default=GenderChoices.Erkak)
    family_status = m.ForeignKey(Family_status, on_delete=m.CASCADE, null=True, blank=True)
    salary = m.IntegerField()
    hired_at = m.DateField()
    passport_id = m.IntegerField(unique=True)
    handicapped = m.ForeignKey(Handicapped, on_delete=m.CASCADE, null=True, blank=True)
    role = m.ForeignKey(Role, on_delete=m.CASCADE, null=True, blank=True)
    job = m.CharField(max_length=100)
    illness = m.ForeignKey(Illness, on_delete=m.CASCADE, null=True, blank=True)
    underages = m.ForeignKey(Underages, on_delete=m.CASCADE, null=True, blank=True)
    organization = m.ForeignKey(Organization, on_delete=m.CASCADE)
    # application = m.ForeignKey()
    work_starts_at = m.TimeField()
    work_ends_at = m.TimeField() 
    taken_money= m.PositiveBigIntegerField(default=0)
    used_money= m.PositiveBigIntegerField(default=0)
    def __str__(self):  #obyektga string qaytaradi, shu obyekta o'tgan xodim nomini qaytaradi
        return f"{self.first_name} {self.last_name}"



