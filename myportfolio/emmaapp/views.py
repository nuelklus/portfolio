from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail,BadHeaderError
from .forms import ContactForm
from .models import PDF
from django.views.generic import TemplateView,CreateView,FormView,ListView
from django.urls import reverse_lazy,reverse

# Create your views here.

class IndexView(TemplateView):
    template_name = "emmaapp/index.html"

class ContactFormView(FormView):
    template_name = "emmaapp/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy('emmaapp:sameindex')

    def form_valid(self, form):
        clean_form = form.cleaned_data

        print(clean_form)
        return super().form_valid(form)

class PDFCreateView(CreateView):
    model = PDF
    fields = '__all__'
    success_url = reverse_lazy('emmaapp:sameindex')
    template_name = 'emmaapp/createpdf.html'

class PDFListView(ListView):
    context_object_name = 'docz'
    model = PDF
    template_name = 'emmaapp/pdflist.html'
    #     subject = clean_form.get('subject', '')
    #     message = clean_form.get('message', '')
    #     from_email = clean_form.get('email' '')
    #     if subject and message and from_email:
    #         try:
    #             send_mail(subject, message, from_email, ['nuelklus@gmail.com'])
    #         except BadHeaderError:
    #             return HttpResponse('Invalid header found.')
    #         # return HttpResponseRedirect('/contact/thanks/')
    #          #returning respons on the create view(parent class)
    #     else:
    #         # In reality we'd use a form class
    #         # to get proper validation errors.
    #         return HttpResponse('Make sure all fields are entered and valid.')
