from django import forms
from .models import Contact

# create ContactForm

class ContactForm(forms.Form):
     name = forms.CharField(
            max_length=100,
            widget=forms.TextInput({'class': 'form-control','placeholder': 'Enter your name'}))
     email = forms.EmailField(
            max_length=100,
            widget=forms.TextInput({'class': 'form-control','placeholder': 'Enter your email'}))
     subject = forms.CharField(
            max_length=100,
            widget=forms.TextInput({'class': 'form-control','placeholder': 'Enter your subject'}))
     message = forms.CharField(
            max_length=2000,
            widget=forms.Textarea({'class': 'form-control'}),
            help_text='Write here your message!'
    )
