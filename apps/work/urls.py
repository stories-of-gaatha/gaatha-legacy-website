from django.urls import path
from apps.work import views

urlpatterns = [
    path("", views.WorkList.as_view(), name="work_list"),
    path("<pk>/", views.WorkDetail.as_view(), name="work_detail"),
]
