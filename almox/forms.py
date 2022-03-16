from django import forms
from almox.models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Item
