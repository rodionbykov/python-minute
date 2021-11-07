from django.urls import path

from . import views

urlpatterns = [
    path("<int:month_number>", views.index_by_number),
    path("<str:month>", views.index, name="index")
]
