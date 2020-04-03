from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from neighbourhood import views
from rest_framework.authtoken.views import obtain_auth_token
from django.views.generic.base import TemplateView



urlpatterns = [
    # path('',views.index,name='index'),
    # path('signup/',views.index,name='signup'),
    path('api/v1/hoods/', views.NeighbourhoodList.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('.*', TemplateView.as_view(template_name='home.html'), name='home')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)






