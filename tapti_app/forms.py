from django import forms
from .models import Item, Category


class ContactForm(forms.Form):

    name                = forms.CharField(max_length=100)
    email_id            = forms.EmailField(required=True)
    subject             = forms.CharField(max_length=200)
    mobile_number       = forms.CharField(max_length=17)
    message             = forms.CharField(widget=forms.Textarea, required=False)
