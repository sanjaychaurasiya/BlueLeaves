from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import SensorSerializer, FarmBlockSerializer, AddSensorSerializer, FarmModuleSerializer
from farm.models import Sensor, AddSensor, FarmBlock, FarmModule


class SensorList(generics.ListCreateAPIView):
    """Class to List and Create Sensors
    Accepts - GET and POST requests."""
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = [IsAuthenticated]


class SensorDetails(generics.RetrieveUpdateDestroyAPIView):
    """Class to get the details of individual items
    Accepts - GET, PUT and DELETE requests. """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = [IsAuthenticated]


class AddSensorList(generics.ListCreateAPIView):
    """Class to List and Create Sensors
        Accepts - GET and POST requests."""
    queryset = AddSensor.objects.all()
    serializer_class = AddSensorSerializer
    permission_classes = [IsAuthenticated]


class AddSensorDetails(generics.RetrieveUpdateDestroyAPIView):
    """Class to get the details of individual items
        Accepts - GET, PUT and DELETE requests. """
    queryset = AddSensor.objects.all()
    serializer_class = AddSensorSerializer
    permission_classes = [IsAuthenticated]


class FarmBlockList(generics.ListCreateAPIView):
    """Class to List and Create Sensors
        Accepts - GET and POST requests."""
    queryset = FarmBlock.objects.all()
    serializer_class = FarmModuleSerializer
    permission_classes = [IsAuthenticated]


class FarmBlockDetails(generics.RetrieveUpdateDestroyAPIView):
    """Class to get the details of individual items
        Accepts - GET, PUT and DELETE requests. """
    queryset = FarmBlock.objects.all()
    serializer_class = FarmBlockSerializer
    permission_classes = [IsAuthenticated]


class FarmModuleList(generics.ListCreateAPIView):
    """Class to List and Create Sensors
        Accepts - GET and POST requests."""
    queryset = FarmModule.objects.all()
    serializer_class = FarmModuleSerializer
    permission_classes = [IsAuthenticated]


class FarmModuleDetails(generics.RetrieveUpdateDestroyAPIView):
    """Class to get the details of individual items
        Accepts - GET, PUT and DELETE requests. """
    queryset = FarmModule.objects.all()
    serializer_class = FarmModuleSerializer
    permission_classes = [IsAuthenticated]

