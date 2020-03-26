from django.urls import path,re_path
from .import views

urlpatterns = [
    path('searchbusiness/', views.search_business, name="search_business"),
    re_path(r'^business/(\d+)',views.single_business,name='singlebusiness'),
    path('add/business',views.add_business,name='addbusiness')
    
]
