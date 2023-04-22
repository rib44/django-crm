from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(Label="", max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Email'}))
    first_name = forms.CharField(Label="", max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(Label="", max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
   