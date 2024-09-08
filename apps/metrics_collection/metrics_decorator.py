import time
from functools import wraps

from .tasks import save_metrics_task

metrics_data = {
    'function_name': '',
    'calls': 0,
    'total_time': 0,
    'errors': 0
}


def metrics_collector(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        metrics_data['function_name'] = func.__name__
        metrics_data['calls'] += 1

        try:
            return func(*args, **kwargs)
        except Exception:
            metrics_data['errors'] += 1
            raise
        finally:
            end_time = time.time()
            execution_time = end_time - start_time
            metrics_data['total_time'] += execution_time

            # Send metrics to Celery task for asynchronous saving
            save_metrics_task.delay(
                function_name=metrics_data['function_name'],
                calls=metrics_data['calls'],
                total_time=metrics_data['total_time'],
                errors=metrics_data['errors']
            )

    return wrapper
