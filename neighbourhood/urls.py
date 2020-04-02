from django.urls import path, re_path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'Neighbourhoods', views.NeighbourhoodList, basename='Neighbourhoods')

urlpatterns = [
    path('api/v1/create_hood/', views.NeighbourhoodList.as_view()),
    re_path(r'api/', include(router.urls)),
    re_path('api/v1/manage_hood/hood-id/(?P<pk>[0-9]+)/', views.HoodManager.as_view())
]

