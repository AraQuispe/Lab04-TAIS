from django import forms
from .models import Product, Combos

class ComboForm(forms.ModelForm):
    class Meta:
        model = Combos
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
