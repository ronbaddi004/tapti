from django.urls import reverse
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.db.models import Q

from .forms import CategoryForm
from .models import Category, Item, Slider

# Create your views here.
def index(request):
    
    latest_items = Item.objects.filter(my_category__name__icontains="latest")

    top_selling = Item.objects.filter(Q(my_category__name__icontains="top") | Q(my_category__name__icontains="selling"))

    categories = Category.objects.filter(display_on_navbar=True)

    sliders = Slider.objects.all()

    return render(request, 'index.html', {'title': "Home", 'latest_items': latest_items, 'top_selling': top_selling, 'categories': categories, 'sliders': sliders})


def items_list(request):

    items = Item.objects.all()

    categories = Category.objects.filter(display_on_navbar=True)

    return render(request, 'items_list.html', {'items': items, 'categories': categories})


def category_detail(request, id):

    print(request)

    category = get_object_or_404(Category, id=id)

    categories = Category.objects.filter(display_on_navbar=True)

    return render(request, "category.html", {'category': category, 'categories': categories})


def about_us(request):

    categories = Category.objects.filter(display_on_navbar=True)

    our_favorites = Item.objects.filter(my_category__name__icontains="favorite")

    return render(request, "about.html", {'categories': categories, 'items': our_favorites})


def contact_us(request):

    categories = Category.objects.filter(display_on_navbar=True)

    our_favorites = Item.objects.filter(my_category__name__icontains="favorite")

    return render(request, "contact.html", {'categories': categories, 'items': our_favorites})

# def create_category(request):
#     """
#     This function based view is used for creation of Category.
#     """
#     form = CategoryForm(request.POST or None)

#     if request.method == 'POST':

#         if form.is_valid():

#             Category.objects.create(
#                 name=form.cleaned_data.get('name'),
#                 description=form.cleaned_data.get('description'),
#             )

#             return HttpResponse(detail={"Successfully Created!!"}, status=201)

#     return render(request, "category_create.html", {'form': form, 'title': "Create Category"})
