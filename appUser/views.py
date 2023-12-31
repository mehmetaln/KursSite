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


def loguotUser(request):
    logout(request)
    return redirect("loginPage")






def registerPage(request):

    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password1 =request.POST.get("password1")
        password2 = request.POST.get("password2") 
        
        boolnum = boolup = False
        boolchar = True
        if fname and lname and email and username and password1 and password2:
            char = ["*;:@?ı/"]    
            if password1 == password2:
                for i in password1:
                    if i.isupper():
                        boolup = True
                    if i.isnumeric():
                        boolnum = True
                    if i in char:
                        boolchar = False
                if boolup and boolnum  and boolchar and len(password1)>=6:
                    if not User.objects.filter(username = username).exists():
                        if not User.objects.filter(email =email).exists():
                            user = User.objects.create_user(first_name =fname, username = username, last_name = lname, email = email, password=password1)
                            user.save()
                            messages.success(request,"Kayıt işleminiz başarı ile tamamlandı")
                            return redirect("loginPage")
                        else:
                            messages.error(request,"Bu e-posta adresi ile kayıtlı bir üye var.")
                    else:
                        messages.error(request,"Bu Kullanıcı Adı ile kayıtlı bir üye var.")
                else:
                    messages.error(request,"E-Posta ve Kullanıcı Adı alanları boş bırakılamaz ve paroalnız 6 haneden buyuk olmalı aynı zmanda Tc'niz 11 haneli olmalı")
            else:
                messages.error(request,"Şifreler uyuşmuyor")
        else:
            messages.error(request,"Tüm Alanları Doldurunuz")
    context ={}
    return render(request, "user/register.html", context)
