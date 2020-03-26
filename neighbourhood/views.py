from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Neighbourhood
from .serializer import NeighbourhoodSerializer
# Create your views here.

class NeighbourhoodList(APIView):
    def get(self, request, format=None):
        hoods = Neighbourhood.objects.all()
        serializers =  NeighbourhoodSerializer(hoods, many=True)
        return Response(serializers.data)