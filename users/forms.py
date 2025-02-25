from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegForm(UserCreationForm):
    first_name = forms.CharField(label='',  max_length=255, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label= '', max_length=255, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
		
        super(UserRegForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

    

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label='', max_length=255, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'})) 
    last_name = forms.CharField(label='', max_length=255, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

    def __init__(self, *args, **kwargs):
		
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

class ProfileForm(forms.ModelForm):
    phone = forms.CharField(label='', max_length=255, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}))
    address1 = forms.CharField(label='', max_length=255, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address 1'}))
    address2 = forms.CharField(label='', max_length=255, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address 2'}), required=False)
    state = forms.CharField(label='', max_length=255, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'State'}))
    city = forms.CharField(label='', max_length=255, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}))
    country = forms.CharField(label='', max_length=255, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Country'}))
    # image = forms.ImageField(upload_to='profile_pic', default='default.jpg')

    
    class Meta:

        model = Profile
        fields = ['phone', 'address1', 'address2', 'state', 'city', 'country', 'image']


class UserInfoForm(forms.ModelForm):
    phone = forms.CharField(label='', max_length=255, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}))
    email = forms.CharField(label='', max_length=255, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    address1 = forms.CharField(label='', max_length=255, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address 1'}))
    address2 = forms.CharField(label='', max_length=255, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address 2'}), required=False)
    state = forms.CharField(label='', max_length=255, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'State'}))
    city = forms.CharField(label='', max_length=255, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}))
    # zipcode = forms.CharField(label='', max_length=255, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zip Code'}))
    country = forms.CharField(label='', max_length=255, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Country'}))

    class Meta:
        model = Profile
        fields = ['phone', 'email', 'address1', 'address2', 'state', 'city', 'country']
        exclude = ['user', 'image', 'is_staff']