from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):
    shipping_fullname = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Fullname'}))
    shipping_email = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    shipping_address1 = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address 1'}))
    shipping_address2 = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address 2'}))
    shipping_city = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'city'}))
    shipping_state = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'State'}))
    shipping_zipcode = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zipcode'}))
    shipping_country = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Country'}))
    
    class Meta:
        model = ShippingAddress
        fields = ('shipping_fullname', 'shipping_email', 'shipping_address1', 'shipping_address2', 'shipping_city', 'shipping_state', 'shipping_zipcode', 'shipping_country')
        exclude = ('user',)

class PaymentForm(forms.Form):
    card_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name on Card'}), required=True)
    card_number = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Number on Card'}))
    card_exp_date = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Card Expiration Date'}))
    card_cvv_number = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Card CVV'}))
    card_address1 = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Card address1'}))
    card_address2 = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Card address2'}), required=False)
    card_city = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Card City'}))
    card_state = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Card State'}))
    card_zipcode = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Card Zipcode'}))
    card_country = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Card Country'}))