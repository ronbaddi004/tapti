from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.db.models import Q

from .forms import ContactForm
from .models import Category, Item, Slider, Contact


def form_validation(cleaned_data):

    name = cleaned_data.get('name')

    email_id = cleaned_data.get('email_id')

    subject = cleaned_data.get('subject')

    message = cleaned_data.get('message')

    mobile_number = cleaned_data.get('mobile_number')

    Contact.objects.create(name=name, email_id=email_id, mobile_number=mobile_number, subject=subject, message=message)


# Create your views here.
def index(request):
    
    latest_items = Item.objects.filter(my_category__name__icontains="latest")

    top_selling = Item.objects.filter(Q(my_category__name__icontains="top") | Q(my_category__name__icontains="selling"))

    categories = Category.objects.filter(display_on_navbar=True)

    sliders = Slider.objects.all()

    if request.method == "GET":

        form = ContactForm()

    else:

        form = ContactForm(request.POST)

        if form.is_valid():

            form_validation(form.cleaned_data)

            return redirect('home')

    return render(request, 'index.html', {'title': "Home", 'latest_items': latest_items, 'top_selling': top_selling, 'categories': categories, 'sliders': sliders, 'form': form})


def items_list(request):

    query = request.GET.get('q')

    item_list = None

    if query:

        item_list = Item.objects.filter(Q(name__icontains=query) | Q(my_category__name__icontains=query))

    else:

        item_list = Item.objects.all()

    page = request.GET.get('page', 1)

    paginator = Paginator(item_list, 5)

    try:

        items = paginator.page(page)

    except PageNotAnInteger:

        items = paginator.page(1)

    except EmptyPage:

        items = paginator.page(paginator.num_pages)

    categories = Category.objects.filter(display_on_navbar=True)

    if request.method == "GET":

        form = ContactForm()

    else:

        form = ContactForm(request.POST)

        if form.is_valid():

            form_validation(form.cleaned_data)

            return redirect('items-list')

    return render(request, 'items_list.html', {'items': items, 'categories': categories, 'form': form})


def category_detail(request, id):

    category = get_object_or_404(Category, id=id)

    categories = Category.objects.filter(display_on_navbar=True)

    if request.method == "GET":

        form = ContactForm()

    else:

        form = ContactForm(request.POST)

        if form.is_valid():

            form_validation(form.cleaned_data)

            return redirect('category-detail')

    return render(request, "category.html", {'category': category, 'categories': categories, 'form': form})


def about_us(request):

    categories = Category.objects.filter(display_on_navbar=True)

    our_favorites = Item.objects.filter(my_category__name__icontains="favorite")

    if request.method == "GET":

        form = ContactForm()

    else:

        form = ContactForm(request.POST)

        if form.is_valid():

            form_validation(form.cleaned_data)

            return redirect('about-us')

    return render(request, "about.html", {'categories': categories, 'items': our_favorites, 'form': form})


def contact_us(request):

    categories = Category.objects.filter(display_on_navbar=True)

    our_favorites = Item.objects.filter(my_category__name__icontains="favorite")

    if request.method == "GET":

        form = ContactForm()

    else:

        form = ContactForm(request.POST)

        if form.is_valid():

            form_validation(form.cleaned_data)

            return redirect('contact-us')

    return render(request, "contact.html", {'categories': categories, 'items': our_favorites, 'form': form})

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
