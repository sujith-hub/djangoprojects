from django.shortcuts import render
from django.shortcuts import redirect
from .models import logindetails
# Create your views here.

def loginpage(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        logindetails(
            username=request.POST.get('username'),
            password=request.POST.get('password'),
        ).save()
        return render(request,'login.html')
