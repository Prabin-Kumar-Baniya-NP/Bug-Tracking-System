from django import forms
from product.models import Product
from django.forms import ModelForm
from company.models import Company
from django.contrib.auth import get_user_model
User = get_user_model()

class ProductCreationForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
    
    def __init__(self, requested_user_id, *args, **kwargs):
        super(ProductCreationForm, self).__init__(*args, **kwargs)
        self.fields['company'].queryset = Company.objects.filter(administrator = requested_user_id)
        self.fields['administrator'].queryset = User.objects.filter(id = requested_user_id)

class ProductUpdationForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
    
    def __init__(self, requested_user_id, product_id, *args, **kwargs):
        super(ProductUpdationForm, self).__init__(*args, **kwargs)
        administrator = Product.objects.get(id = product_id).administrator.all()
        non_administrator = User.objects.filter(product_assigned = product_id)
        self.fields['company'].queryset = Company.objects.filter(administrator = requested_user_id)
        self.fields['administrator'].queryset = administrator | non_administrator