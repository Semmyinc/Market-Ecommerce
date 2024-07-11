from django import forms
from .models import Category, Product





class ProductForm(forms.ModelForm):
 
    class Meta:
        model = Product
        fields = ['user', 'name', 'description', 'image', 'price', 'promo', 'promo_price', 'category']
        # fields = '__all__'
        # exclude = ('user',)
        widgets = {
            'user': forms.Select(attrs={'class':'form-control', 'placeholder':'user'}),
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'name'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            # 'image': forms.ImageField(attrs={'class':'form-control'}),
            'price': forms.TextInput(attrs={'class':'form-control'}),
            # 'promo': forms.RadioSelect(attrs={'class':'form-control'}),
            # 'promo_price': forms.IntegerInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
        }
        # labels = {
        #     'user':'',
        #     'name':''
        # }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'user': forms.Select(attrs={'class':'form-control', 'placeholder':'user'}),
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Category Name'})
        }
        labels = {
            'name': ''
        }
