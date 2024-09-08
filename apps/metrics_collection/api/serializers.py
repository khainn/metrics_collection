from rest_framework import serializers


class MetricsCollectionRequest(serializers.Serializer):
    function_name = serializers.CharField()


class MetricsCollectionResponse(serializers.Serializer):
    function_name = serializers.CharField()
    calls = serializers.IntegerField()
    average_time = serializers.FloatField()
    errors = serializers.IntegerField()
