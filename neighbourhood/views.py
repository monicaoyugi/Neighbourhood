from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from .models import  Neighbourhood
from .serializer import NeighbourhoodSerializer
# Create your views here.

class NeighbourhoodList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, format=None):
        hoods = Neighbourhood.objects.all()
        serializers =  NeighbourhoodSerializer(hoods, many=True)
        return Response(serializers.data)
        
    def post(self, request, format=None):
        serializers = NeighbourhoodSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

        # "token": "d9afe015425bd886af1abb30490ca7b008bfce05"