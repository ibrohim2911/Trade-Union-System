from django.db import models

class money_history(models.Model):
    current_money = models.PositiveBigIntegerField()
    spent_money = models.PositiveBigIntegerField()

class Organization(models.Model):
    
    organization_name = models.CharField(max_length=200)
    phone_number = models.BigIntegerField()
    money = models.ForeignKey(money_history, on_delete=models.PROTECT)
    monthly_money = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.organization_name