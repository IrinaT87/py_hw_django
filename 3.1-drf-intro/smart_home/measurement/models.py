from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=70, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"sensor: {self.sensor} temperature: {self.temperature} time: {self.created_at}"