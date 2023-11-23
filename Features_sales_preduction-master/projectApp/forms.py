from django import forms
from .models import *

class Features_sales_preductionForm(forms.Form):
    TV = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'TV'}))
    Radio = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Radio'}))
    Newspaper = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Newspaper'}))
    
    