from django.db.models import Q
import django_filters
from django_filters.views import FilterView
from django.views import generic
from django.shortcuts import render

from apps.work.models import Work, Tag, WorkType, WorkFeature
from apps.main.models import Page

def grouped(l, n):
    group = []
    for i in range(0, len(l), n):
        group.append(l[i:i+n])
    return group

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
    filterset_class = WorkFilter
    ordering = ["-id"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        context["work_types"] = WorkType.objects.all()
<<<<<<< HEAD
        cover_description_empty_filter = Q(cover_description__isnull=True) | Q(cover_description='')
        work_with_cover_description = Work.objects.exclude(cover_description_empty_filter)
        work_with_no_cover_description = Work.objects.filter(cover_description_empty_filter)

        data = []
        non_description = {"type": "non-description", "items": []}
        with_description = {"type": "description", "items": []}
        non_description_start_index = 0
        non_description_batch_size = 4
        description_start_index = 0
        description_batch_size = 1
        column_size = 5
        for i in range(0, Work.objects.count(), column_size):
            if i % column_size == 0:
                non_description["items"].append(
                    work_with_no_cover_description[
                        non_description_start_index:non_description_batch_size
                    ]
                )
                data.append(non_description)
                with_description["items"].append(
                    work_with_cover_description[
                        description_start_index:description_batch_size
                    ]
                )
                data.append(with_description)
                description_start_index += 1
                non_description_start_index += 4
                description_batch_size += 1
                non_description_batch_size += 4
                non_description = {"type": "non-description", "items": []}
                with_description = {"type": "description", "items": []}
        context["works"] = data
=======
        print (grouped(context["object_list"], 10))
        context["grouped_object"] = grouped(context["object_list"], 10)
>>>>>>> Added work-scroll
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
        context["work_features"] = WorkFeature.objects.filter(work=self.object)
        return context


def home(request, *args, **kwargs):
    page = Page.objects.filter(page_type=Page.PageType.DASHBOARD)
    context = {
        "page": page.first if page else None,
        "works": Work.objects.filter(is_featured_in_dashboard=True).order_by('-id')[:4],
    }
    return render(request, "home.html", context)
