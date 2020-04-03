import datetime
from django.http import HttpResponse, JsonResponse
from .permissions import IsAdminOrReadOnly

from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Neighbourhood,Business,
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

    @classmethod
    def get_extra_actions(cls):
        return []

    serializer_class = NeighbourhoodSerializer
    def get(self, request, format=None):
        hoods = Neighbourhood.objects.all()
        serializer = self.serializer_class(data=hoods)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
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
    
# def search_results(request):
#     if 'business' in request.GET and request.Get["business"]:
#         search_term = request.GET.get("business")
#         search_categories = Business.search_business(search_term)
#         message = f"{search_term}"
#         return render(request,'searchbusiness.html',{"message":message,"business":searched_business})
#     else:
#          message ="You haven't searched for any categories"
#          return render(request, 'searchbusiness.html',{"message":message,"businesssearched":search_categories})

def search_business(request):
    
    if 'business' in request.GET and request.GET["business"]:
        category = request.GET.get("business")
        searched_category = Business.search_by_category(category)
        message = f"{category}"
        
        return render(request, 'searchbusiness.html',{"message":message,"businesssearched":search_categories})
     
def single_business(request,businessid):
    single_business=Business.single_business(businessid)
    return render(request,'singlebusiness.html',{'singlebusiness':single_business})

def add_business(request):
    current_user = request.user
    if request.method == 'POST':
        form = business(request.POST,request.FILES)
        if form.is_valid():
            project =form.save(commit=False)
            project.editor =current_user
            project.save()
            return redirect('home')
    else:
        form = business()
    return render(request,'postbusiness.html',{"form":form}) 



