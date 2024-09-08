from django.urls import path

from .views import MetricsCollectionDetailAPIView, TestAPIView

urlpatterns = [
    path('metric-collection', MetricsCollectionDetailAPIView.as_view(), name='metric_collection'),
    path('test-metric-collection', TestAPIView.as_view(), name='test_metric_collection'),

]
