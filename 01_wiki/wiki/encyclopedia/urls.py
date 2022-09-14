from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.entryPage, name="entryPage"),
    path("search/", views.search, name="search")
]
