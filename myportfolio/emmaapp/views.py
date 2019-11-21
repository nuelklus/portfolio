from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail,BadHeaderError
from .models import Contact
from .forms import ContactForm
from django.views.generic import TemplateView,CreateView

# Create your views here.

class IndexView(TemplateView):
    template_name = "emmaapp/index.html"

class ContactCreateView(CreateView):
    template_name = "emmaapp/contact.html"
    form_class = ContactForm # helps you to connect to the form
    model = Contact # connecting to the contact model

    def form_valid(self, form):
        clean_form = form.cleaned_data
        print(clean_form)
        subject = clean_form.get('subject', '')
        message = clean_form.get('message', '')
        from_email = clean_form.get('email' '')
        if subject and message and from_email:
            try:
                send_mail(subject, message, from_email, ['nuelklus@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            # return HttpResponseRedirect('/contact/thanks/')
            return super().form_valid(form) #returning respons on the create view(parent class)
        else:
            # In reality we'd use a form class
            # to get proper validation errors.
            return HttpResponse('Make sure all fields are entered and valid.')
