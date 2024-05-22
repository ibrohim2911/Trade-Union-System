from django.db import models
from organization.models import Organization
# Create your models here.
class Employee(models.Model):    #xodim uchun class/model yaratildi va malumotlari olindi
    
    class handicappedChoice(models.TextChoices):
        zero = "0", "Nogiron emas"
        second = "3", "2-darajali"
        third = "2", "3-darajali"
    class roleChoice(models.TextChoices):
        none = "0", "nazoratga olinmagan"
        iron = "4", "temir daftari"
        women = "4", "ayollar va yoshlar daftari"

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    age = models.DateField()
    is_married = models.BooleanField(default=False)
    is_divorced = models.BooleanField(default=False)
    salary = models.IntegerField()
    hired_at = models.DateField()
    passport_id = models.CharField(max_length=20)
    handicapped = models.CharField(max_length=1, choices=handicappedChoice.choices, default=handicappedChoice.zero)
    role = models.CharField(max_length=100, choices=roleChoice.choices,default=roleChoice.none)
    current_health = models.CharField(max_length=100)
    has_illness = models.BooleanField(default=True)
    family_health = models.CharField(max_length=100)
    underages = models.IntegerField()
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)
    overall_bal = models.IntegerField(default=0)

    def __str__(self):  #obyektga string qaytaradi, shu obyekta o'tgan xodim nomini qaytaradi
        return f"{self.first_name} {self.last_name}"
