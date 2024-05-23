from django.db import models
from django.core.validators import FileExtensionValidator
from phonenumber_field.modelfields import PhoneNumberField


from organization.models import Organization
from utils.models import BaseModel
from utils import choices

# Create your models here.


class Role(BaseModel):  # temir daftar
    title = models.CharField(max_length=100)
    file = models.FileField(
        upload_to="role/", validators=[FileExtensionValidator(allowed_extensions=["pdf", "jpg", "jpeg"])], null=True, blank=True)

    def __str__(self):
        return self.title


class FamilyStatus(BaseModel):  # Oilaviy holati
    title = models.CharField(max_length=100)
    file = models.FileField(
        upload_to="role/", validators=[FileExtensionValidator(allowed_extensions=["pdf", "jpg", "jpeg"])], null=True, blank=True)

    def __str__(self):
        return self.title


class Handicapped(BaseModel):  # nogironligi
    title = models.CharField(max_length=100)
    file = models.FileField(
        upload_to="role/", validators=[FileExtensionValidator(allowed_extensions=["pdf", "jpg", "jpeg"])], null=True, blank=True)

    def __str__(self):
        return self.title


class Illness(BaseModel):  # Kasalligi
    title = models.CharField(max_length=100)
    file = models.FileField(
        upload_to="role/", validators=[FileExtensionValidator(allowed_extensions=["pdf", "jpg", "jpeg"])], null=True, blank=True)

    def __str__(self):
        return self.title


class Employee(BaseModel):  # xodim uchun class/model yaratildi va malumotlari olindi
    full_name = models.CharField(max_length=256)
    job = models.CharField(max_length=128)
    phone_number = PhoneNumberField(unique=True, region="UZ")
    gender = models.CharField(
        max_length=128, choices=choices.GenderChoices.choices, default=choices.GenderChoices.MALE)

    age = models.IntegerField(default=0)
    salary = models.IntegerField(default=0)
    passport = models.CharField(max_length=9, unique=True)

    taken_money = models.DecimalField(
        max_digits=10, decimal_places=2)  # Qancha pul olingan
    used_money = models.DecimalField(
        max_digits=10, decimal_places=2)  # Unga ajratilgan pul
    hired_at = models.DateField()  # ishga kirgan vaqti

    work_starts_at = models.TimeField()
    work_ends_at = models.TimeField()

    handicapped = models.ForeignKey(
        Handicapped, on_delete=models.CASCADE, related_name="handicapped")
    role = models.ForeignKey(
        Role, on_delete=models.CASCADE, related_name="role")
    illness = models.ForeignKey(
        Illness, on_delete=models.CASCADE, related_name="illness")
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name="organization")
    family_status = models.ForeignKey(
        FamilyStatus, on_delete=models.CASCADE, related_name="status")

    def __str__(self):
        return self.full_name


class Underages(BaseModel):  # guvohnoma
    quantity = models.IntegerField()
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="employee")

    def __str__(self):
        return self.employee.full_name


class UnderageFile(BaseModel):
    file = models.FileField(
        upload_to="role/", validators=[FileExtensionValidator(allowed_extensions=["pdf", "jpg", "jpeg"])], null=True, blank=True)
    underages = models.ForeignKey(
        Underages, on_delete=models.CASCADE, related_name="underages")
