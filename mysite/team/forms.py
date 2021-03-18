from django import forms
from team.models import Team
from django.forms import ModelForm
from django.contrib.auth import get_user_model
User = get_user_model()

class TeamCreationForm(ModelForm):
    class Meta:
        model = Team
        fields = "__all__"
    
    def __init__(self, requested_user_id, *args, **kwargs):
        super(TeamCreationForm, self).__init__(*args, **kwargs)
        self.fields['administrator'].queryset = User.objects.filter(id = requested_user_id)