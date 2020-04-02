import datetime

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Neighbourhood
from .serializer import NeighbourhoodSerializer
from rest_framework import status



@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user.id
    user = request.user
    print(datetime.date.today(), "####################################################################")
    date = datetime.date.today()
    posts = Post.objects.all()
    if Profile.objects.filter(user = request.user).count() == 0:
        prof = Profile(user=request.user)
        prof.save()
    return render(request, 'index.html',{"date":date, "posts": posts})

class NeighbourhoodList(APIView):
    serializer_class = NeighbourhoodSerializer
    def get(self, request, format=None):
        hoods = Neighbourhood.objects.all()
        serializer = self.serializer_class(data=hoods)
        return Response(serializer.data,status=status.HTTP_200_OK)
