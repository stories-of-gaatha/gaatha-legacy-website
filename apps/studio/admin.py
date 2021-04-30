from django.contrib import admin
from apps.studio.models import SocialMedia, People


class SocialMediaAdmin(admin.ModelAdmin):
    """
    Social media  admin
    """

    list_display = ["id", "url", "icon"]
    list_display_links = ["id", "url"]


class PeopleAdmin(admin.ModelAdmin):
    """
    People  admin
    """

    list_display = ["id", "name", "job_title", "description"]
    list_display_links = ["id", "job_title"]


admin.site.register(SocialMedia, SocialMediaAdmin)
admin.site.register(People, PeopleAdmin)
