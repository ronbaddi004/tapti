from django.urls import path

from .views import index, contact_us, category_detail, about_us, items_list


urlpatterns = [
    path('', index, name="home"),
    path('about', about_us, name="about-us"),
    path('contact', contact_us, name="contact-us"),
    path('items/list', items_list, name="items-list"),
    path('category/<int:id>', category_detail, name="category-detail")
]