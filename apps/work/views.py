from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse

from apps.work.models import Work


# Create your views here.

class WorkList(generic.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'work.html')
