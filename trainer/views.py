from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def trainers(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def trainer_id(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def service(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def booking_time(request):
    return HttpResponse("Hello, world. You're at the polls index.")