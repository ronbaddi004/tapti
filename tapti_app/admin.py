from django.contrib import admin

from .models import Item, Category, Slider, Contact

# Register your models here.
admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Slider)
admin.site.register(Contact)