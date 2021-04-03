from django import forms
from product.models import Product
from ticket.models import Ticket
from django.forms import ModelForm
from django.contrib.auth import get_user_model
User = get_user_model()

class BugReportForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description',  'product_name', 'submitted_by']
    
    def __init__(self, requested_user_id, *args, **kwargs):
        super(BugReportForm, self).__init__(*args, **kwargs)
        requested_user = User.objects.get(id = requested_user_id)
        self.fields['product_name'].queryset = Product.objects.filter(administrator = requested_user)
        self.fields['submitted_by'].queryset = User.objects.filter(id= requested_user_id)

class TicketUpdationForm(ModelForm):
    class Meta:
        model = Ticket
        fields = "__all__"
    
    def __init__(self, requested_user_id, *args, **kwargs):
        super(TicketUpdationForm, self).__init__(*args, **kwargs)
        self.fields['product_name'].queryset = User.objects.get(id=requested_user_id).product_assigned.all()
        self.fields['submitted_by'].queryset = User.objects.filter(id= requested_user_id)
