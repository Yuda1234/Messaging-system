from rest_framework import serializers
from .models import ChetMessage


class ChetMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChetMessage
        fields = '__all__'
