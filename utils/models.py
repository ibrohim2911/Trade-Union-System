from django.db import models


class BaseModel(models.Model):
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
