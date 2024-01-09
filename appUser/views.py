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


def logoutUser(request):
    logout(request)
    return redirect("indexPage")






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

def hesapPage(request):
    if request.method == "POST":
        submit = request.POST.get("submit")
        if submit =="emailSubmit":
            email = request.POST.get("email")
            password = request.POST.get("password")
            if email and password:
                if request.user.check_password(password):
                    request.user.email = email
                    print(request.user.email)
                    request.user.save()
                    messages.success(request, "Emailiniz başarı ile değiştirildi") 
                    logout(request)
                    return redirect('loginPage')
                else:
                    messages.error(request,'Girilen Şifre Yanlış')
            else:
                messages.error(request,'Boş Bırakılan alanlar var')   
    
        elif submit == "telSubmit":
            tel =request.POST.get("tel")
            password = request.POST.get("password")
            if tel and password:
                if request.user.check_password(password):
                    request.user.usermy.tel = tel
                    request.user.usermy.save()
                    messages.success(request,"Telefon numaranız başarı ile değiştirildi")
                    logout(request)
                    return redirect("loginPage")
                else:
                     messages.error(request,"Girilen parola yanlış")
            else:
                messages.error(request,"Boş Bırakilan alanlar var")

        elif submit =="passwordSubmit":
            password = request.POST.get("password")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")
            if password and password1 and password2:
                if request.user.check_password(password):
                    if password1 == password2:
                        request.user.set_password(password1)
                        request.user.save()
                        messages.success(request, "PArolanız başarı ile değiştirildi")
                        logout(request)
                        return redirect("loginPage")
                    else:
                        messages.error(request,"Parolalar uyuşmuyor")
                else:
                    messages.error(request,"Girilen Parola Yanlış")
            else:
                messages.error(request,"Bos bırakılan alanlar var.")
        
        elif submit == "userSubmit":
            username = request.POST.get("username")
            password =request.POST.get("password")
            if username and password:
                if request.user.check_password(password):
                    request.user.username = username
                    request.user.save()
                    messages.success(request, "Kullanıcı adınız başarıyla değiştirildi")
                    logout(request)
                    return redirect ("loginPage")
                else:
                    messages.error(request,"Geçersiz Şifre")
            else:
                messages.error(request,"Bos bırakılan yerler var")
                
        elif submit == "imagesubmit":
            image=request.FILES['image']
            password =request.POST.get("password")
            if image and password:
                if request.user.check_password(password):
                    request.user.image = image
                    request.user.save()
                    messages.success(request,"PRofil Fotografınız değiştirildi")
                    return redirect("hesapPage")
                else:
                    messages.error(request,"Girilen şifre yanlış")
            else:
                messages.error(request,"Boş Bırakılan alanlar var")
                
                
        return redirect("hesapPage")

        
                
    context = {}
    return render(request,"user/hesap.html",context)