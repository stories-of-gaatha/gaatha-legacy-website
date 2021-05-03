from django.db import models
from django_enumfield import enum


class Page(models.Model):
    """
    Page model
    """

    # Page type
    class PageType(enum.Enum):
        DASHBOARD = 0
        ABOUT = 1
        PEOPLE = 2

        __labels__ = {DASHBOARD: "Dashboard", ABOUT: "About", PEOPLE: "People"}

    content = models.TextField()

    # Page type
    page_type = enum.EnumField(
        PageType, verbose_name="Select page", null=True, blank=True, unique=True
    )

    class Meta:
        verbose_name = "Page setting"
        verbose_name_plural = "A - Page settings"

    def __str__(self):
        return str(self.id)
