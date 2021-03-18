from django import forms
from company.models import Company
from django.forms import ModelForm
from django.contrib.auth import get_user_model
User = get_user_model()

class CompanyCreationForm(ModelForm):
    class Meta:
        model = Company
        fields = "__all__"
    
    def __init__(self, requested_user_id, *args, **kwargs):
        super(CompanyCreationForm, self).__init__(*args, **kwargs)
        self.fields['administrator'].queryset = User.objects.filter(id = requested_user_id)