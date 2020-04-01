from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('search/', views.search,name = "search"),
    #path('allergen-search/', views.allergen_search, name = "allergen-search"),
    path('search/keyword-search/', views.keyword_search, name = "keyword-search"),

]
