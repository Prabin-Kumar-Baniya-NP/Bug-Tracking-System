from django.forms import ModelForm
from django import forms
from user.models import User

class UserCreationForm(ModelForm):
    """
    For the creation of user
    """
    class Meta:
        model = User
        fields = ["username", "password", "first_name", "last_name", "email", "address", "birth_date"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.fields["first_name"].widget = forms.TextInput(attrs={'id':"first_name"})
        self.fields["last_name"].widget = forms.TextInput(attrs={'id':"last_name"})
        self.fields["username"].widget = forms.TextInput(attrs={'id':"username"})
        self.fields["password"].widget = forms.PasswordInput(attrs={'id':"password"})
        self.fields["email"].widget = forms.EmailInput(attrs={'id':"email"})
        self.fields["address"].widget = forms.TextInput(attrs={'id':"address"})
        self.fields["birth_date"].widget = forms.DateInput(attrs={'id':"birth_date"})

class UserUpdationForm(ModelForm):
    """
    Updates the user information
    """
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "address", "birth_date", "about_me"]