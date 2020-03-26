from django.shortcuts import render,redirect
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
     
def single_business(request,businessid):
    single_business=Business.single_business(businessid)
    return render(request,'singlebusiness.html',{'singlebusiness':single_business}) 


def addbusiness(request):
    current_user = request.user
    if request.method == 'POST':
        form = addbusiness(request.POST,request.FILES)
        if form.is_valid():
            project =form.save(commit=False)
            project.editor =current_user
            project.save()
            return redirect('home')
    else:
        form = NewProjectForm()
    return render(request,'new_project.html',{"form":form})  


