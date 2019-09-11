from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):

    name                = models.CharField(max_length=100)
    description         = models.TextField(max_length=2000, null=True, blank=True)
    display_on_navbar   = models.BooleanField(default=False)
    newly_added         = models.BooleanField(default=False)

    timestamp           = models.DateTimeField(auto_now_add=True)
    updated             = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("category-detail", kwargs={"id": self.id})

    def __str__(self):
        return self.name


class Item(models.Model):

    my_category         = models.ManyToManyField(Category, related_name="item")
    name                = models.CharField(max_length=100)
    image               = models.FileField(upload_to="images/")
    on_sale             = models.BooleanField(default=False)
    newly_added         = models.BooleanField(default=False)

    timestamp           = models.DateTimeField(auto_now_add=True)
    updated             = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Item Name: {self.name}"


class Slider(models.Model):

    my_item             = models.ForeignKey(Item, on_delete=models.CASCADE)

    newly_arrival       = models.BooleanField(default=False)
    image               = models.FileField(upload_to="images/slider/")
    header              = models.CharField(max_length=200)
    description         = models.TextField(max_length=2000, null=True, blank=True)