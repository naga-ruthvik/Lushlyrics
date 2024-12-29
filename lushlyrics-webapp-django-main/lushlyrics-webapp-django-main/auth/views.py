from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm-password']
        myuser=User.objects.create_user(username=username,email=email,password=password)
        myuser.save()
        return redirect('/login/')
    return render(request,'signup.html',)


def handlelogin(request):
    checkpass=True
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        myuser=authenticate(username=username,password=password)
        
        if myuser:
            login(request,myuser)
            return redirect('/')
        else:
            checkpass=False
    return render(request,'login.html',{'checkpass':checkpass})


def handlelogout(request):
    logout(request)
    return redirect('/login')