from django.contrib import admin
from apps.work.models import Tag, WorkType, Picture, Work, WorkFeature
from apps.work.forms import WorkAdminForm


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

    list_display = ["id", "description"]
    list_display_links = ["id", "description"]
    search_fields = ["id", "description"]


class WorkFeatureInline(admin.TabularInline):
    model = WorkFeature
    extra = 0


class WorkAdmin(admin.ModelAdmin):
    """
    Work  admin
    """

    list_display = [
        "id",
        "artwork",
        "cover_image",
        "cover_description",
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
