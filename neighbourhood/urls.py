from django.urls import path
from .import views

urlpatterns = [
    path('searchbusiness/', views.search_business, name="search_business"),
    
]
