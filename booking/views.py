from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def booking(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def cancellation_of_reservation(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def confirm_booking(request, user_id):
    return HttpResponse("Hello, world. You're at the polls index.")

def booking_details(request):
    return HttpResponse("Hello, world. You're at the polls index.")
