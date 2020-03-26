
from django.conf import settings
from django.urls import path
from neighbourhood import views 
from rest_framework.authtoken.views import obtain_auth_token
from django.views.generic.base import TemplateView


urlpatterns = [
    path('api/v1/hoods', views.NeighbourhoodList.as_view()),
    path('.*', TemplateView.as_view(template_name="home.html"), name="home")
]
=======
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.index,name='signup'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

