from celery import shared_task
from django.db import transaction

from .models import MetricsCollection


@shared_task
def save_metrics_task(function_name, calls, total_time, errors):
    with transaction.atomic():
        metric, _ = MetricsCollection.objects.get_or_create(function_name=function_name)

        metric.calls += calls
        metric.errors += errors
        if metric.calls > 0:
            metric.average_time = ((metric.average_time * (metric.calls - calls)) + total_time) / metric.calls
        metric.save()
