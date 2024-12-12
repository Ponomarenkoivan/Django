from django.urls import path

from . import views

urlpatterns = [
    path("", views.trainers, name="trainers"),

    path("<id>", views.trainer_id, name="trainer_id"),

    path("<id>/<service_id>", views.service, name="service"),

    path("<id>/<service_id>/booking", views.booking_time, name="booking_time"),

]