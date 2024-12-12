from django.urls import path

from . import views

urlpatterns = [
    path("", views.booking, name="booking"),

    path("<booking_id>", views.booking_details, name="booking_details"),

    path("<booking_id>/accept", views.confirm_booking, name="confirm_booking"),

    path("<booking_id>/cancel", views.cancellation_of_reservation, name="cancellation_of_reservation"),
]