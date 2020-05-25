from django import forms

from GenrateInvoice.models import CustomerDetails
from GenrateInvoice.models import ProductInfo

class CustomerDetailsForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Customer Name',
            'required': True
        }
    ))
    address = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Address',
            'required': True
        }
    ))
    panNo = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'PAN NO',
            'required': True
        }
    ))
    Gstin = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'GSTIN',
            'required': True
        }
    ))
    class Meta:
        model=CustomerDetails
        fields="__all__"

class ProductInfoForm(forms.ModelForm):
    prodName= forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Product Name',
            'required': True
        }
    ))
    prodCode = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Product Code',
            'required': True
        }
    ))
    class Meta:
        model=ProductInfo
        fields="__all__"
