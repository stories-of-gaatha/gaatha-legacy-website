from django import forms

from tinymce.widgets import TinyMCE

from apps.studio.models import People


class PeopleAdminForm(forms.ModelForm):
    """
    People admin form
    """

    description = forms.CharField(widget=TinyMCE(attrs={"cols": 80, "rows": 30}), required=False)

    class Meta:
        model = People
        fields = "__all__"
