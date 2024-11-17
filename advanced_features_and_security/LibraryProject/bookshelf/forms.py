
from django import forms
from .models import Book

class ExampleForm(forms.Form):
    q = forms.CharField(max_length=100, required=False)