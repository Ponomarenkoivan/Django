from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def user_page(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def specific_user(request, user_id):
    return HttpResponse("Hello, world. You're at the polls index.")

def login_page(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("logged_in")
        else:
            return render(request, 'login.html')

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponse("You are now logged out.")
    return HttpResponse("login first")

def register_page(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')


    user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
    user.save()
    return HttpResponse("Hello, world. You're at the polls index.")