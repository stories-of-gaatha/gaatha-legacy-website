import django_filters
from django_filters.views import FilterView
from apps.studio.models import People

class PeopleList(FilterView):
    model = People
    template_name = "studio/people_list.html"
    paginate_by = 10
    ordering = ["-id"]
