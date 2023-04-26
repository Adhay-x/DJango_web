from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def register(request):
    if request.method == 'POST':
         uname = request.POST.get('username')
         email=request.POST.get('email')
         pass1=request.POST.get('password1')
         pass2=request.POST.get('password2')

         if pass1 != pass2:
             return HttpResponse('Your password and confirm password are not the same!!')
         else:
             myuser = User.objects.create_user(uname, email, pass1)
             myuser.save()
             return redirect ('login')
    return render(request, 'signup.html')

def Login(request):
     if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user = authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")
          
     return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

      
