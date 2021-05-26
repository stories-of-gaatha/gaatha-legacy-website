from django.contrib import admin

from apps.contact.models import (
    ContactNumber,
    Contact,
    EmailQuery
)
from apps.contact.forms import ContactAdminForm


@admin.register(ContactNumber)
class ContactNumberAdmin(admin.ModelAdmin):
    pass


@admin.register(EmailQuery)
class EmailQuery(admin.ModelAdmin):
    pass


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    form = ContactAdminForm
