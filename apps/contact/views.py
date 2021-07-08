from django.db import models
from django.views.generic import ListView

from apps.contact.models import Contact


class ContactList(ListView):
    model = Contact
    template_name = 'contact/contact_list.html'
