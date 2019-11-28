from django.db import models
from django.utils import timezone
from django.urls import reverse
#from django.core.urlresolvers import reverse

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=2000)

    # created_date = models.DateTimeField(default=timezone.now)
    # published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

class PDF(models.Model):
    mycv = models.FileField(upload_to='PDFS/CVS/')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    # def get_absolute_url(self):
    #     return reverse("emmaapp:sameindex",kwargs={})
