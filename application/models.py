from django.db import models
from utils.models import BaseModel


class Aplication(BaseModel):
    title = models.CharField(max_length=256)
    description = models.TextField()
    status = models.CharField(max_length=128)