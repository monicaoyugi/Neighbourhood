from django.conf import settings
from django.urls import path
from neighbourhood import views 
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/v1/hoods', views.NeighbourhoodList.as_view()),
]
