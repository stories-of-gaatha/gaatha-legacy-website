from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError

from tinymce.widgets import TinyMCE
from apps.work.models import Work, Picture


class WorkAdminForm(forms.ModelForm):
    """
    Work admin form
    """

    list_description = forms.CharField(widget=TinyMCE(attrs={"cols": 80, "rows": 30}), required=False)

    class Meta:
        model = Work
        fields = "__all__"

    def clean_artwork(self):
        artwork = self.cleaned_data.get("artwork", False)
        if artwork:
            extension = str(artwork).split('.')[-1]
            file_type = extension.lower()
            if file_type not in settings.ARTWORK_IMAGE_FILE_TYPES:
                raise ValidationError(f'Unsupported file format:Supported are{settings.ARTWORK_IMAGE_FILE_TYPES}')
            return artwork

    def clean_cover_image(self):
        cover_image = self.cleaned_data.get("cover_image", False)
        if cover_image:
            extension = str(cover_image).split('.')[-1]
            file_type = extension.lower()
            if file_type not in settings.COVERIMAGE_IMAGE_FILE_TYPES:
                raise ValidationError(f'Unsupported file format:Supported are{settings.COVERIMAGE_IMAGE_FILE_TYPES}')
            return cover_image


class PictureAdminForm(forms.ModelForm):
    """
    Work picture admin form
    """

    description = forms.CharField(widget=TinyMCE(attrs={"cols": 80, "rows": 30}), required=False)

    class Meta:
        model = Picture
        fields = "__all__"
