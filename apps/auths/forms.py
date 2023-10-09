# Django
from typing import Any
from django import forms

# Local
from .models import Client


class AuthsForm(forms.Form):
    """Form for authenticate user."""

    username = forms.CharField(
        max_length=50,
    )
    password = forms.CharField(
        widget=forms.PasswordInput, 
        min_length=8, 
        max_length=32
    )
        

class RegForm(forms.Form):
    """Form for registration users."""

    username = forms.CharField(
        max_length=50, 
        min_length=8,
        required=True
    )
    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput,
        required=True
    )
    first_name = forms.CharField(
        max_length=50,
        required=True
    )
    last_name = forms.CharField(
        max_length=50,
        required=True
    )
    password = forms.CharField(
        widget=forms.PasswordInput, 
        min_length=8, 
        max_length=32,
        required=True
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if Client.objects.filter(username=username).exists():
            raise forms.ValidationError(
                message=f'username {username} is already exist'
            )
        return username
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if Client.objects.filter(email=email).exists():
            raise forms.ValidationError(
                message=f'email {email} already exist'
            )
        return email
    
