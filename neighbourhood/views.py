from django.shortcuts import render
from .models import Business

# Create your views here.

def search_results(request):
    if 'business' in request.GET and request.Get["business"]:
        search_term = request.GET.get("business")
        searched_business = Business.search_business(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message,"business":searched_business})
    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{"message":message})
