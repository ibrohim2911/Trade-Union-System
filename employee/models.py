from django.db import models as m

# Create your models here.
class Employee(m.Model):    #xodim uchun class/model yaratildi va malumotlari olindi
    first_name = m.CharField(max_length=50)
    last_name = m.CharField(max_length=50)
    phone_number = m.BigIntegerField(max_length=12)
    age = m.DateTimeField()
    is_married = m.BooleanField(default=False)
    children = m.IntegerField(max_length=2)
    is_dicorced = m.BooleanField(default=False)
    salary = m.IntegerField(max_length=30)
    hired_at = m.DateTimeField()
    passport_id = m.IntegerField(max_length=7)
    is_handicapped = m.BooleanField(default=False)
    role = m.CharField(max_length=100)
    current_health = m.CharField(max_length=100)
    illness = m.CharField(max_length=100)
    family_health = m.CharField(max_length=100)
    underages = m.IntegerField(max_length=1)
    def __str__(self):  #obyektga string qaytaradi, shu obyekta o'tgan xodim nomini qaytaradi
        return f"{self.first_name} {self.last_name}"
