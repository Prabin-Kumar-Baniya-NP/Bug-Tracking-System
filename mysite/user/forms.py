from django.forms import ModelForm
from django import forms
from user.models import User
from django.contrib.auth.forms import UserCreationForm as UserCreate, UserChangeForm


class UserCreationForm(UserCreate):
    """
    For the creation of user
    """
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'email': "Email Address",
        }

class UserUpdationForm(UserChangeForm):
    """
    Updates the user information
    """
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', "address", "birth_date", "about_me"]
        labels = {
            'email': "Email Address",
        }