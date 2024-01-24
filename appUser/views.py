from django.shortcuts import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from django.db.models import Count
from django.core.mail import send_mail # bu fonksiyonu mail göndermek için kullanıyoruz views kısmında
from KursSite.settings import EMAIL_HOST_USER # settingsden çektigimiz host kısmımız bunu send mail içerisinde kullanacağız
from django.utils.crypto import get_random_string # random string ifadeler getirmemize yarar () parantez içerisnde kaç haneli olmasını istediğimizi yazarız
from appUser.models import *



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
        
            if password1 == password2:
                for i in password1:
                    if i.isupper():
                        boolup = True
                    if i.isnumeric():
                        boolnum = True

                if boolup and boolnum  and boolchar and len(password1)>=6:
                    if not User.objects.filter(username = username).exists():                            
                            random_link =get_random_string(44)  # random linkimizin string kısmı 
                            emaillink = "http://"+request.get_host()+"/emailActive/"+random_link #request.get_host methodu bize girişli olan kullanıcın host bilgilerini verir
                            # diger kısımlar https gibi bizim ell ile yazdıgımız linklerin kısımları
                            
                            user = User.objects.create_user(first_name =fname, username = username, last_name = lname, email = email, password=password1)
                            user.is_active = False # kullanıcıyı oluştur ama aktif hale getirme diyoruz bu kısımda maili onayladıktan sonra aktif hale getireceğiz 
                            user.save() # userı kaydet ama tabi aktif olarak degil yapmıza saglar
                            
                            usermy = Usermy(user =user, user_active =random_link) # Usermy içerisinde ki objeşleri buradaki viewsde lazım olan yerlere eşitliyoruz
                            usermy.save() # usermy kısmına kaydediyoruz burada oneöli olan useravtivite
                            
                                    
                            send_mail(  # Bu kısmda ise mesajımızı düzenleyioruz  
                            "Kayıdı tamamlamak için mailenizez gelen linki onaylayınız", # Buraya başlık veya konu gelicek
                            f"Lütfen email hesabınızı onaylayınız: {emaillink}", # Bu kısım mailde gözükecek Kısım
                            EMAIL_HOST_USER, # Settingsden çektiğimiz olmassa olmaz host kısmız 
                            [email], # Burası ilgili olan kullanıcın maili
                            fail_silently=False, # bunu boşver
                        )

                            
                            
                            messages.success(request,"Kayıt işlemlerinin tamamlanması için lütfen maila adresinizi onaylayınjz")
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


def emailActive(request,elink): # Bu ksımda maile bir gelen link onaylandıgını kontrol edecegiz e link değişkeni urlden geliyor
     # Eğer verilen 'elink' değeriyle eşleşen bir Usermy objesi varsa
    if Usermy.objects.filter(user_active = elink).exists(): # Bizim hali hazırda user_Active kısmını kontrol ediyoruz
        # Bu objeyi al
        myuser = Usermy.objects.get(user_active = elink) # burada user_Actşveye elink degişkenimiz tanımlıyoruz 
        #İlgili kullanıcının is_active özelliğini True olarak ayarla
        myuser.user.is_active = True # bu kısımda mailonaylandıktan sonra bu kısmı true çeviriyoruz
        # Kullanıcı değişikliklerini kaydet
        myuser.user.save() # burada tekrar kaydeiyoruz activesi true olacak şekilde 
        messages.success(request, "Emailiniz başarı ile Onaylandı")
        
    return redirect("loginPage")    




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
                
    imagesubmit = request.POST.get("submit") # Eger profil fotografı değiştireceksem yani dıaşrıdan bir fotograf veya belge gelcekse methodumuz post
     #fakat yüklenen belge veya fotograf için files methodunu kullnamma gerekiyor
    if imagesubmit == "imageSubmit":
        profile_image=request.FILES.get("profile_image") # ÖRnekte ki gibi
        password =request.POST.get("password")
        
        if profile_image and password:
            if request.user.check_password(password):
                request.user.usermy.profile_image = profile_image
                request.user.usermy.save()
                messages.success(request,"Profil Fotografınız değiştirildi")
                return redirect("hesapPage")
            else:
                messages.error(request,"Girilen şifre yanlış")
        else:
            messages.error(request,"Boş Bırakılan alanlar var")
            
                
        return redirect("hesapPage")

        
                
    context = {
    }
    return render(request,"user/hesap.html",context)