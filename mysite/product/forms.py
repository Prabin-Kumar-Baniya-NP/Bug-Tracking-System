from django import forms
from product.models import Product
from django.forms import ModelForm
from django.contrib.auth import get_user_model
User = get_user_model()

class ProductCreationForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
    
    def __init__(self, requested_user_id, *args, **kwargs):
        super(ProductCreationForm, self).__init__(*args, **kwargs)
        self.fields['administrator'].queryset = User.objects.filter(id = requested_user_id)