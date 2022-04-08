from django.http import Http404

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Airplane
from .serializers import AirplaneSerializer


class AirplanePagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 50


class AirplaneList(APIView):
    pagination_class = AirplanePagination

    def get(self, request):
        airplane = Airplane.objects.all()
        serializer = AirplaneSerializer(airplane, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AirplaneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AirplaneDetail(APIView):

    def get_object(self, pk):
        try:
            return Airplane.objects.get(pk=pk)
        except Airplane.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        airplane = self.get_object(pk)
        serializer = AirplaneSerializer(airplane)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        airplane = self.get_object(pk)
        serializer = AirplaneSerializer(airplane, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        airplane = self.get_object(pk)
        airplane.delete()
        return Response({
            "status": "success",
            "message": f"Airplane with id={pk} has been deleted successfully!"
        }, status=status.HTTP_204_NO_CONTENT)
