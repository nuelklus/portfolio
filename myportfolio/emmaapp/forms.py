from django import forms
from .models import Contact

# create ContactForm

class ContactForm(forms.ModelForm):
    class Meta():
        model = Contact
        fields = ('name','email','subject','message',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your message'}),
        }
