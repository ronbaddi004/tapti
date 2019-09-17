from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

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


class Contact(models.Model):

    name                = models.CharField(max_length=100)
    email_id            = models.EmailField()
    mobile_number       = models.CharField(max_length=17, null=True, validators=[phone_regex])
    subject             = models.CharField(max_length=100)
    message             = models.CharField(max_length=1000, blank=True, null=True)

    created_at          = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"from: {self.name} subject: {self.subject}"
