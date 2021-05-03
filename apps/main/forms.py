from django import forms
from django.utils.translation import ugettext_lazy as _
from tinymce.widgets import TinyMCE
from apps.main.models import Page


class PageAdminForm(forms.ModelForm):
    """
    Page admin form
    """

    content = forms.CharField(widget=TinyMCE(attrs={"cols": 80, "rows": 30}))

    class Meta:
        model = Page
        fields = "__all__"
