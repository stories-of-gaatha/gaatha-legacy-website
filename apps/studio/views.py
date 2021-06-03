from django.views.generic import ListView
from django.shortcuts import render

from apps.studio.models import (
    People
)
from apps. work.models import Work
from apps.main.models import Page


class PeopleList(ListView):
    model = People
    template_name = "studio/people_list.html"
    paginate_by = 10
    ordering = ["-id"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = Page.objects.filter(page_type=Page.PageType.PEOPLE)
        print(context['page'])
        return context

def about(request, *args, **kwargs):
    page = Page.objects.filter(page_type=Page.PageType.ABOUT)
    context = {
        "page": page.first if page else None,
        "works": Work.objects.filter(is_featured_in_dashboard=True).order_by('id')[:5],
    }
    return render(request, "studio/about.html", context)
