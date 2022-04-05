from django.contrib import admin
from .models import Super
from super_types.models import Type 

admin.site.register(Super)
admin.site.register(Type)
