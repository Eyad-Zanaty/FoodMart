from django import forms
from .models import Customers

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model= Customers
        fields= ['subscribe']
        widget= {'subscribe': forms.CheckboxInput(attrs={"class": "form-check-input", "id": "subscribe"})}