from django import forms
from .models import Contact

# create ContactForm

class ContactForm(forms.Form):
     name = forms.CharField(max_length=500)
     email = forms.EmailField(max_length=500)
     subject = forms.CharField(max_length=500)
     message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your message!'
    )




    # class Meta():
    #     model = Contact
    #     fields = '__all__'
    # #
    #     widgets = {
    #         'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your name'}),
    #         'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
    #         'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your subject'}),
    #         'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your message'}),
    #     }
