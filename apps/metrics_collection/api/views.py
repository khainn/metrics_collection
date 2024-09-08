from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from common.exceptions import BadRequest
from common.serializers import ErrorResponse
from .serializers import MetricsCollectionRequest, MetricsCollectionResponse
from apps.metrics_collection.models import MetricsCollection
from apps.metrics_collection.utils import gen_random_string


@extend_schema(tags=['MetricsCollection'])
class MetricsCollectionDetailAPIView(APIView):

    @extend_schema(parameters=[MetricsCollectionRequest],
                   responses={200: MetricsCollectionResponse, 400: ErrorResponse, 500: ErrorResponse})
    def get(self, request):
        query_params = request.query_params.dict()
        serializer = MetricsCollectionRequest(data=query_params)
        if not serializer.is_valid():
            raise BadRequest(400000, error_detail=serializer.errors)

        function_name = serializer.validated_data.get('function_name')
        metrics = MetricsCollection.objects.filter(function_name=function_name).first()
        if not metrics:
            raise BadRequest(400003)
        response = MetricsCollectionResponse(metrics)
        return Response(response.data)


@extend_schema(tags=['Test'])
class TestAPIView(APIView):
    @extend_schema(responses={400: ErrorResponse, 500: ErrorResponse})
    def post(self, request):
        random_string = gen_random_string(10, ['a', 'b', 'c', 'd', 'e', 'f'])
        return Response({
            'function_name': 'gen_random_string',
            'results': random_string
        })
