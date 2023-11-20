from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('form')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    return render(request, 'login.html')


def sub(request):
    return render(request, 'sub.html')


def form(request):
    return render(request, 'form.html')


def order(request):
    return render(request, 'order.html')


def returns(request):
    return render(request, 'return.html')


def enquiry(request):
    return render(request, 'enquiry.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, "user name already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)

            user.save();
            return redirect('login')
        else:
            messages.info(request, 'password not matched')
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
