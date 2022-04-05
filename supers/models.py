from django.db import models
from super_types.models import Type

class Super(models.Model):
    name = models.CharField(max_length=20)
    ability = models.CharField(max_length=255)
    super_type = models.ForeignKey(Type, on_delete=models.CASCADE)
