from django import forms
from .models import Item, Category

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('my_category', 'name', 'image',)


class CategoryForm(forms.ModelForm):
    
    name                = forms.CharField(max_length=100)
    description         = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Category
        fields = ('name', 'description',)
