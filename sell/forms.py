from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class EditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','profile_pic']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name','image','description','price','category']
