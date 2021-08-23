from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from accounts.models import Product




def login(request):
    if request.method == 'POST':
        usernameVar = request.POST.get('usernameText')
        passwordVar = request.POST.get('passwordText')
        user = auth.authenticate(username=usernameVar, password=passwordVar)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'UserName Taken')
                return redirect('/accounts/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('/accounts/register')
            else:
                user = User.objects.create_user(username=username,password=password, email=email, first_name=first_name,last_name=last_name )
                user.save();
                print('User Created')
                return redirect('/accounts/login')
        else:
            messages.info(request, 'password not matching...')
            return redirect('/accounts/register')

    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def shop(request):
    products =  Product.objects.all()
    return render(request, 'shop.html' ,{"products": products}) 