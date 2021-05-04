from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse
from apps.work.models import Work, Tag, WorkType
from apps.main.models import Page
import django_filters
from django_filters.views import FilterView


class WorkFilter(django_filters.FilterSet):
    """
    Work Filter
    """

    tags = django_filters.CharFilter(field_name="tags__id", lookup_expr="in")
    work_types = django_filters.CharFilter(field_name="work_type", lookup_expr="in")

    class Meta:
        model = Work
        fields = ["tags", "work_types"]


class WorkList(FilterView):
    model = Work
    template_name = "works/list.html"
    paginate_by = 10
    filterset_class = WorkFilter
    ordering = ["-id"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        context["work_types"] = WorkType.objects.all()
        return context

class WorkDetail(generic.DetailView):
    """
    Work detail
    """
    model = Work
    template_name = "works/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        context["work_types"] = WorkType.objects.all()
        return context

def home(request, *args, **kwargs):
    page = Page.objects.filter(page_type=Page.PageType.DASHBOARD)
    context = {
        "page": page.first if page else None,
        "works": Work.objects.filter(is_featured_in_dashboard=True),
    }
    return render(request, "home.html", context)

def about(request, *args, **kwargs):
    page = Page.objects.filter(page_type=Page.PageType.ABOUT)
    context = {
        "page": page.first if page else None,
        "works": Work.objects.filter(is_featured_in_dashboard=True),
    }
    return render(request, "home.html", context)
