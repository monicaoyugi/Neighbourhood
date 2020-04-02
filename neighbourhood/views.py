from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Neighbourhood
from .serializer import NeighbourhoodSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly


class NeighbourhoodList(APIView):
   
    @classmethod
    def get_extra_actions(cls):
        return []
    
    
    permission_classes = (IsAdminOrReadOnly,)
    
    def get(self, request, format=None):
        hoods = Neighbourhood.objects.all()
        serializers = NeighbourhoodSerializer(hoods, many=True)
        return Response(serializers.data)



    def post(self, request, format=None):
        serializers = NeighbourhoodSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class HoodManager(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, pk, format=None):
        hood = self.get_hood(pk)
        serializers = NeighbourhoodSerializer(hood)
        return Response(serializers.data)

    def get_hood(self, pk):
        try:
            return Neighbourhood.objects.get(pk=pk)
        except Neighbourhood.DoesNotExist:
            return Http404

   
 
    def put(self, request, pk, format=None):
        hood = self.get_hood(pk)
        serializers = NeighbourhoodSerializer(hood, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
   

    def delete(self, request, pk, format=None):
        hood = self.get_hood(pk)
        hood.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

   