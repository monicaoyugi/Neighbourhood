from neighbourhood import views 
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.index,name='signup'),
    path('api/v1/hoods', views.NeighbourhoodList.as_view()),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

