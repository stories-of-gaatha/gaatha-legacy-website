import django_filters
from django_filters.views import FilterView
from django.shortcuts import render

from apps.studio.models import (
    People
)
from apps. work.models import Work
from apps.main.models import Page


class PeopleList(FilterView):
    model = People
    template_name = "studio/people_list.html"
    paginate_by = 10
    ordering = ["-id"]


def about(request, *args, **kwargs):
    page = Page.objects.filter(page_type=Page.PageType.ABOUT)
    context = {
        "page": page.first if page else None,
        "works": Work.objects.filter(is_featured_in_dashboard=True).order_by('id')[:4],
    }
    return render(request, "studio/about.html", context)
