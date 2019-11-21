from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=2000)

    # created_date = models.DateTimeField(default=timezone.now)
    # published_date = models.DateTimeField(blank=True, null=True)

# Redirect on completing contact forms
    def get_absolute_url(self):
        return reverse('index')

    def __str__(self):
        return self.name
