from django.db import models
from super_types.models import Type

class Super(models.Model):
    name = models.CharField(max_length=20)
    alter_ego = models.CharField(max_length=255)
    primary_ability = models.CharField(max_length=255)
    secondary_ability = models.CharField(max_length=255)
    catchphrase = models.CharField(max_length=255)
    super_type = models.ForeignKey(Type, on_delete=models.CASCADE)
