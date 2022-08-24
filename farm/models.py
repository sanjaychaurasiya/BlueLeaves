import random
import string
import uuid
from django.db import models
from secrets import token_urlsafe


# def random_id():
#     return ''.join(random.choices(string.ascii_lowercase + string.digits, k=10) for _ in range(8))
# m = 0
# random_string =


class Sensor(models.Model):
    """Class to create model for managing sensors"""
    sensor_name = models.CharField(max_length=100)
    group_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.sensor_name


class FarmBlock(models.Model):
    """Class to create a model to add a new farm."""
    m = 0
    m = m + 1
    block_name = models.CharField(max_length=10, default=token_urlsafe(7))
    block_id = models.CharField(max_length=10, default=''.join(f'b{m}'))
    unit_id = models.CharField(max_length=10, default=''.join(f'u{m}'))

    def __str__(self):
        return self.block_name


class FarmModule(models.Model):
    """Class to create Farm Module."""
    module_name = models.CharField(max_length=10, default=token_urlsafe(7))
    block_id = models.ForeignKey('FarmBlock', on_delete=models.CASCADE)
    module_id = models.CharField(max_length=15)

    def __str__(self):
        return self.module_name


class AddSensor(models.Model):
    """Class to Add a new sensor."""
    group_id = models.ForeignKey('Sensor', on_delete=models.CASCADE)
    sensor_id = models.CharField(max_length=100)

    def __str__(self):
        return self.sensor_id
