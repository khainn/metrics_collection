from django.db import models

from common.models import BaseModel


class MetricsCollection(BaseModel):
    function_name = models.CharField(max_length=255)
    calls = models.PositiveIntegerField(default=0)
    average_time = models.FloatField(default=0.0)
    errors = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'metrics_collection'
