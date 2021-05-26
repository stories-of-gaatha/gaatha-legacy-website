from django import forms

from apps.contact.models import Contact


class ContactAdminForm(forms.ModelForm):
    """
    Contact admin form
    """
    class Meta:
        model = Contact
        fields = "__all__"
