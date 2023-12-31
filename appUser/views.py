from django.shortcuts import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from django.db.models import Count




def loginPage(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        rememberme =request.POST.get("rememberme")
        
        user =authenticate(username = username, password = password)
        if user:
            login(request,user)
            messages.success(request,"Giriş Başarılı")
            return redirect ("indexPage")

        else:
            messages.error(request,"Kullanıcı adınız veya şifreniz yanlış")
        
    
    context={}
    return render(request, "user/login.html", context)



def registerPage(request):
    context ={}
    return render(request, "user/register.html", context)
