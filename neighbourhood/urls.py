from django.urls import path, re_path, include
from django.views.generic.base import TemplateView

from . import views
from rest_framework import routers
from neighbourhood import views
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


# router = routers.DefaultRouter(trailing_slash=False)
# router.register(r'Neighbourhoods', views.NeighbourhoodList, basename='Neighbourhoods')

urlpatterns = [
    path('api/v1/create_hood/', views.NeighbourhoodList.as_view()),
    re_path(r'api/', include(router.urls)),
    re_path('api/v1/manage_hood/hood-id/(?P<pk>[0-9]+)/', views.HoodManager.as_view()),
    path('',views.index,name='index'),
    path('api-token-auth/', obtain_auth_token),
    path('signup/',views.index,name='signup'),
    path('.*', TemplateView.as_view(template_name='home.html'), name='home'),
    path('api/v1/hoods', views.NeighbourhoodList.as_view()),
    path('search/business', views.search_business, name="search_business"),
    re_path(r'^business/(\d+)',views.single_business,name='singlebusiness'),
    path('add/business',views.add_business,name='add-business')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
