from django.shortcuts import render
from django.views import generic
from .forms import KeyWordSearchForm
from .models import Restaurant
# Create your views here.

def index(request):
    return render(request,'index.html')

def search(request):
    return render(request,'search.html')

def keyword_search(request):
    '''if post, process data'''
    if request.method == "POST":
        form = KeyWordSearchForm(request.POST)  #populate

        if form.is_valid():
            restaurants = Restaurant.objects.filter(name__icontains = form.cleaned_data['keyword'])
            context = {
                'restaurant_list': restaurants,
                }
            return render(request,'keyword.html',context)
        
    else:
        form = KeyWordSearchForm(initial={'name':"for example: Culvers"})
    context = {
        'form':form,
        'restaurant_list': None,
                }
        
    return render(request,'keyword.html',context)

class RestaurantListView(generic.ListView):
    model = 'Restaurant'
    template_name = "keyword.html"
    
