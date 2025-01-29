from django import forms
from .models import Customers

class CustomerForm(forms.Form):
    class Meta:
        model= Customers
        fields= ['purchase']