from django.shortcuts import render, redirect # return sabit kullandıgımız render ettiğimiz yerlerde eger bir sayfası varsa render kullanıoruz oksa ise redirect kullanıırz oda yönlendirme için 
from appMy.models import * # appmy içerisindeki tüm her şeyi getirmemize yarar
from django.db.models import Count # Bir karekteri kaç kez yazdıgımıza dair sorgular yapmmıza yarar
from django.db.models import Q # ve bağlacını kullanmamıza yarar baızyerlerde
from django.contrib.auth import authenticate, login, logout # girişçıkış ve kontrol işlemlerimiz gerçekleştirmemize yarar
from django.contrib.auth.models import User # User modelinin tüm objelerini getirmemize ve bu sayfada kullanmamız a yarar
from django.contrib import messages # Mesaj gondermek için kullanıyoz
from django.core.mail import send_mail # bu fonksiyonu mail göndermek için kullanıyoruz views kısmında
from KursSite.settings import EMAIL_HOST_USER # settingsden çektigimiz host kısmımız bunu send mail içerisinde kullanacağız
from appUser.forms import KursForm  # Kurs form kullanıcıların kendi adlarına ders kurs paylaşabilmelerini sağlar bu kursformmu formspynden çekiyoruz
# def browsePage(request):
#     context= {}
#     return render(request,"browse.html", context)







def detailPage(request,kid):
    kurs_list = Kurs.objects.filter(id=kid)
    comment_list = Comment.objects.filter(kurs =kurs_list.first())
    kurs_random_list = Kurs.objects.all().order_by("?")
    
    if request.method == "POST":
        
        
        text = request.POST.get("text")
        
        if kurs_list.exists(): # ilgili bir kurs varmı kontrol eder
            kurs = kurs_list.first()      
            comment = Comment(text=text, kurs= kurs, user =request.user)
            comment.save()
               
    
    
        
    context = {
        "comment_list":comment_list,
        "kurs_list": kurs_list,
        "kurs_random_list": kurs_random_list[:6]
    }
    return render (request,"detail.html",context)




def indexPage(request):
    kurs_list =Kurs.objects.all()
    kurs_random_list = Kurs.objects.all().order_by("?")
    onlinecategory_list =OnlineCategory.objects.all()
    facetofacecategory_list =FacetoFaceCategory.objects.all()
    province_list = Province.objects.all()
    
    context = {
        "kurs_list":kurs_list,
        "onlinecategory_list":onlinecategory_list,
        "facetofacecategory_list":facetofacecategory_list,
        "kurs_random_list": kurs_random_list[:8],
        "province_list":province_list
    }
    return render(request, "index.html",context)





def allkursPage(request, oslug=None, pslug=None, fslug=None):
    kurs_list = Kurs.objects.all().order_by('-id')

    if oslug:
        kurs_list = kurs_list.filter(onlinecategory__yslug=oslug)

    elif fslug:
        kurs_list = kurs_list.filter(facetofacecategory__tslug=fslug)

    elif pslug:
        kurs_list = kurs_list.filter(province__islug=pslug)

    query = request.GET.get("query")
    print("Arama Sorgusu:", query)
    if query:
        kurs_list = kurs_list.filter(Q(title__icontains=query))
    
        
    
    onlinecategory_list = OnlineCategory.objects.all()
    facetofacecategory_list = FacetoFaceCategory.objects.all()
    province_list = Province.objects.all()

    context = {
        "kurs_list": kurs_list,
        "onlinecategory_list": onlinecategory_list,
        "facetofacecategory_list": facetofacecategory_list,
        "province_list": province_list,
    }

    return render(request, "allkurs.html", context)


def emailPage(request):
    
    users =User.objects.all().values("email") # User objemizin içerisindeki values degeri email olan tüm kullanıcıların maillerini getirmeye yarar
    users_list = [] # boş liste tanımlıyoruz buryaa atacagız valuesden gelen egerleri
    
    
    for i in list(users): # usersda ki degerleri listeye dönüştürüyoruz 
        users_list.append(i["email"]) # daha sonra listeyi append methoduyla emaile karşılık gelenleri users_liste gönderiyoruz
    
    if request.method == "POST": # Burada formumuzun methodunu kontrol ediyoruz 
        
        konu = request.POST.get("konu") #name leri çekiyoruz
        mesaj = request.POST.get("mesaj") # diger nameyi çekiyoruz
        
        if konu and mesaj:
            try: # try yani dene
                send_mail(  # Bu kısım email gönderme toplu veya tekli olarak görndermemize yarayan kısımdır öncelikle send maili çekmemizgerekiyor
                    konu, # bu kısıma ise name konu olan bölümü çekiyoruz
                    mesaj, # bu kısıma ise namei mesaj olan kısmı çekiyoruz
                    EMAIL_HOST_USER, # bu kısmı çekmek için once settings ayarlarını çekmemiz gerekiyor bu bizim mail gönderebilmemiz için gerekli olan host bölgesi
                    users_list, # burada for ile donderdigimiz user modelinin valuesi email olan degerler tutulur
                    fail_silently =False, # bunu valla bilmiyırum ama gerekli hata ile ilgili galiba
                )
                messages.success(request,"Mesajınız Başarı işe iletildi")
            except:# try olmassa bunu denicek bunlar bizim hata mesajlarından kaçmamıza yarar
                messages.error(request,"Mesajınız gönderilemedi")
        return redirect("emailPage")             
    context = {}
    return render(request,"email.html",context)

def contentPage(request):
    if request.method =="POST":
        form = KursForm(request.POST,request.FILES) # Burada ki Files kısmı resimler veya dosyalar için
        if form.is_valid(): # Buradaki is_valid tüm zorunlu alanların doldurulup doldurulmadıgını kontrol etmek için 
            new_kurs =form.save(commit=False) # veri tabanına hemen bir şeyler kaydetmemize yarayan özellik çok önemli mi billemiyorum burada new kursa formu kaydediyoruz 
            new_kurs.user =request.user # Şuanki kullanıcıya atama yapamıza yardımcı olur  şuanki kullanıcıya kaydettiğimiz formu atıyoruz
            new_kurs.save() # en son kursu kaydediyoruz sayfamıza gidiyor
            messages.success(request,"Kurs Başarı ile eklendi ")
            return redirect('/')
        else:
            messages.error(request,"Form Geçerli degil, Lütfen gerekli bilgileri Doldurunuz")
    else:
        form =KursForm() 
    context = {'form':form}
    return render (request,"mycontent.html",context)













# image = request.POST.get("image")
# title = request.POST.get("title")
# price = request.POST.get("price")
# okategori = request.POST.get("okategori")
# ykategori = request.POST.get("ykategori")
# province = request.POST.get("province")
# text = request.POST.get("text")
# if title and price and okategori and text:
    
#     newKurs=Kurs(image=image,title=title,price=price, onlinecategory = okategori, facetofacecategory = ykategori, province = province, text=text)

# try:
#     newKurs.save()
#     messages.success(request, "Kurs başarıyla eklendi.")
# except:
#     messages.error(request, f"Kurs eklenirken hata oluştu: {e}")
#     return redirect('contentPage')