from django.contrib import admin
from apps.work.models import Tag, WorkType, Picture, Work, WorkFeature
from apps.work.forms import WorkAdminForm, PictureAdminForm
from django.utils.html import format_html


class TagAdmin(admin.ModelAdmin):
    """
    Tag  admin
    """

    list_display = ["id", "name"]
    list_display_links = ["id", "name"]
    search_fields = ["id", "name"]


class WorkTypeAdmin(admin.ModelAdmin):
    """
    Work type  admin
    """

    list_display = ["id", "name"]
    list_display_links = ["id", "name"]
    search_fields = ["id", "name"]


class PictureAdmin(admin.ModelAdmin):
    """
    Picture  admin
    """
    def image_thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" height="100" width="120"/>'
                .format(obj.image.url)
            )
        return ""

    list_display = ["id", "image_thumbnail", 'description']
    list_display_links = ["id", "description"]
    search_fields = ["id", "description"]
    form = PictureAdminForm


class WorkFeatureInline(admin.TabularInline):
    model = WorkFeature
    extra = 0


class WorkAdmin(admin.ModelAdmin):
    """
    Work  admin
    """

    def cover_image_thumbnail(self, obj):
        if obj.cover_image:
            return format_html(
                '<img src="{}" height="100" width="120"/>'
                .format(obj.cover_image.url)
            )
        return ""

    def artwork_thumbnail(self, obj):
        if obj.artwork:
            return format_html(
                '<img src="{}" height="100" width="120"/>'
                .format(obj.artwork.url)
            )
        return ""

    list_display = [
        "id",
        "artwork_thumbnail",
        "cover_image_thumbnail",
        "list_description",
        "is_featured_in_dashboard",
        "work_type",
    ]
    list_display_links = ["id"]
    search_fields = ["id"]
    form = WorkAdminForm
    inlines = [WorkFeatureInline]


admin.site.register(Tag, TagAdmin)
admin.site.register(WorkType, WorkTypeAdmin)
admin.site.register(Picture, PictureAdmin)
admin.site.register(Work, WorkAdmin)
