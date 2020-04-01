from django.contrib import admin
from .models import Restaurant,Allergen,FoodItem
# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Allergen)
admin.site.register(FoodItem)