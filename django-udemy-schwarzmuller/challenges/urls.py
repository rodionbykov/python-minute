from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), # empty root url, list of months
    path("<int:month_number>", views.challenges_by_month_number),
    path("<str:month_name>", views.challenges_by_month_name, name="monthly_challenge")
]
