from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import ModelForm

class UserForm(UserCreationForm):
    
    email = forms.CharField(max_length=30, label='Email-id')
    first_name = forms.CharField(max_length=20, label='First Name')
    last_name = forms.CharField(max_length=20, label='Last Name')
    
    class Meta:
        model = User
        fields = [ 'first_name','last_name','username','email',  'password1', 'password2']

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['company','product', 'capacity']


class LoginForm(forms.Form):
    username = forms.CharField(label = "Username")
    password = forms.CharField(label = "Password",widget = forms.PasswordInput)


class AddOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields=['seller_name', 'quantity', 'message']



    