from django.contrib import admin
from apps.main.models import Page
from apps.main.forms import PageAdminForm


class PageAdmin(admin.ModelAdmin):
    """
    Page admin
    """

    list_display = ["id", "page_type", "content"]
    list_display_links = ["id", "page_type"]
    form = PageAdminForm


admin.site.register(Page, PageAdmin)
