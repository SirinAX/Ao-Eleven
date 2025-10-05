from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','price','stock','description','thumbnail','category','is_featured','brand','rating']
        widgets = {
            'name': forms.TextInput(attrs={'id':'id_name','class':'w-full border rounded-md p-2', 'placeholder':'Product name'}),
            'price': forms.NumberInput(attrs={'id':'id_price','class':'w-full border rounded-md p-2', 'placeholder':'Price', 'min':'0'}),
            'stock': forms.NumberInput(attrs={'id':'id_stock','class':'w-full border rounded-md p-2', 'placeholder':'Stock', 'min':'0'}),
            'description': forms.Textarea(attrs={'id':'id_description','class':'w-full border rounded-md p-2', 'placeholder':'Product description'}),
            'category': forms.Select(attrs={'id':'id_category','class':'w-full border rounded-md p-2'}),
            'thumbnail': forms.URLInput(attrs={'id':'id_thumbnail','class':'w-full border rounded-md p-2', 'placeholder':'Thumbnail URL'}),
            'brand': forms.TextInput(attrs={'id':'id_brand','class':'w-full border rounded-md p-2', 'placeholder':'Brand name'}),
            'rating': forms.NumberInput(attrs={'id':'id_rating','class':'w-full border rounded-md p-2', 'placeholder':'Rating', 'step':'0.01', 'min':'0', 'max':'5'}),
            'is_featured': forms.CheckboxInput(attrs={'id':'id_is_featured','class':'h-4 w-4'}),
        }
