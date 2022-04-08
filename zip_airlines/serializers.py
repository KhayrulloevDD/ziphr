import math

from rest_framework import serializers

from .models import Airplane


class AirplaneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Airplane
        fields = ['id', 'passengers', 'capacity', 'consumption_per_minute', 'able_to_fly']
