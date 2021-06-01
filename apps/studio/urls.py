from django.urls import path
from apps.studio import views

urlpatterns = [
    path("", views.about, name="about_us"),
    path("people/", views.PeopleList.as_view(), name="people_list"),
]
