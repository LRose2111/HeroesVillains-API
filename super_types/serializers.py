from rest_framework import serializers
from .models import Type

class Super_TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id','type']