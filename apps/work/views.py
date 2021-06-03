from django.db.models import Q
import django_filters
from django_filters.views import FilterView
from django.views import generic
from django.shortcuts import render

from apps.work.models import Work, Tag, WorkType
from apps.main.models import Page


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
        work_with_cover_description = Work.objects.exclude(
            Q(cover_description__isnull=True) | Q(cover_description__exact="")
        )
        work_with_no_cover_description = Work.objects.filter(
            Q(cover_description__exact="")
        )

        data = []
        non_description = {"type": "non-description", "item": []}
        non_description_start_index = 0
        non_description_batch_size = 4
        description_start_index = 0
        description_batch_size = 1
        for i in range(Work.objects.count()):
            if i % 5 == 0:
                non_description["item"].append(
                    work_with_no_cover_description[
                        non_description_start_index:non_description_batch_size
                    ]
                )
                data.append(non_description)
                data.append(
                    {
                        "type": "description",
                        "item": {
                            work_with_cover_description[
                                description_start_index:description_batch_size
                            ]
                        },
                    }
                )
                description_start_index += 1
                non_description_start_index += 4
                description_batch_size += 1
                non_description_batch_size += 4
                non_description = {"type": "non-description", "item": []}
        context["works"] = data
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
        "works": Work.objects.filter(is_featured_in_dashboard=True).order_by('-id')[:4],
    }
    return render(request, "home.html", context)
