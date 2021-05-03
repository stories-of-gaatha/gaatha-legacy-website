from django.contrib import admin
from apps.studio.models import SocialMedia, People
from apps.studio.forms import PeopleAdminForm


class SocialMediaAdmin(admin.ModelAdmin):
    """
    Social media  admin
    """

    list_display = ["id", "url", "social_media_type"]
    list_display_links = ["id", "social_media_type"]


class PeopleAdmin(admin.ModelAdmin):
    """
    People  admin
    """

    list_display = ["id", "name", "job_title", "description"]
    list_display_links = ["id", "job_title"]
    form = PeopleAdminForm


admin.site.register(SocialMedia, SocialMediaAdmin)
admin.site.register(People, PeopleAdmin)

