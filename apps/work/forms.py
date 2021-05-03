from django import forms
from django.utils.translation import ugettext_lazy as _
from tinymce.widgets import TinyMCE
from apps.work.models import Work


class WorkAdminForm(forms.ModelForm):
    """
    Work admin form
    """

    cover_description = forms.CharField(widget=TinyMCE(attrs={"cols": 80, "rows": 30}))

    class Meta:
        model = Work
        fields = "__all__"
