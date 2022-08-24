from rest_framework import serializers
from farm.models import Sensor, AddSensor, FarmBlock, FarmModule


class SensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        fields = '__all__'


class AddSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddSensor
        fields = '__all__'


class FarmBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmBlock
        fields = '__all__'


class FarmModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmBlock
        fields = '__all__'

