from django.shortcuts import render
from .models import Business

# Create your views here.

def search_results(request):
    if 'business' in request.GET and request.Get["business"]:
        search_term = request.GET.get("business")
        search_categories = Business.search_business(search_term)
        message = f"{search_term}"
        return render(request,'searchbusiness.html',{"message":message,"business":searched_business})
    else:
         message ="You haven't searched for any categories"
         return render(request, 'searchbusiness.html',{"message":message,"businesssearched":search_categories})

