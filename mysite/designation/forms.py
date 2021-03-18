from django import forms
from designation.models import Designation
from django.forms import ModelForm
from team.models import Team
from django.contrib.auth import get_user_model
User = get_user_model()

class DesignationCreationForm(ModelForm):
    class Meta:
        model = Designation
        fields = "__all__"
    
    def __init__(self, requested_user_id, *args, **kwargs):
        super(DesignationCreationForm, self).__init__(*args, **kwargs)
        self.fields["team"].queryset = Team.objects.filter(administrator = requested_user_id)
        self.fields['administrator'].queryset = User.objects.filter(id = requested_user_id)