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



def sepetPage(request):
    sepet_list =Sepet.objects.filter(user=request.user) # Girişli olan kullanıcın sepetni ver bana demek  yoksa tğüm hepsinin sepetini veirir
    
    
 

    context = {
         "sepet_list":sepet_list, 

    }
    return render(request,"sepet.html",context)


def satinAl(request,bid):
    
    urun = Kurs.objects.filter(id=bid) 
    sepet = Sepet.objects.all()
  
    messages.success(request,"Başarı ile Alındı")
    if sepet:
        sepet.delete()
        return redirect("sepetPage")
    
   
def siparisPage(request):
    
    
    
    context ={}
    return render(request,"siparis.html", context)

def sepetDelete(request,sid): # silme fonksşyouzmu  sepeti
    sepet =Sepet.objects.get(id=sid)
    sepet.delete()
    
    
    return redirect("sepetPage")


def detailPage(request,kid):
    kurs_list = Kurs.objects.filter(id=kid)
    comment_list = Comment.objects.filter(kurs =kurs_list.first())
    kurs_random_list = Kurs.objects.all().order_by("?")
    
    
    
    if request.method == "POST":
        
        submit =request.POST.get("submit")
        text = request.POST.get("text")
        
        if submit =="commentSubmit":
            if request.user:
                if kurs_list.exists(): # ilgili bir kurs varmı kontrol eder
                    kurs = kurs_list.first()      
                    comment = Comment(text=text, kurs= kurs, user =request.user)
                    comment.save()
                    
                    kurs.comment_num +=1
                    kurs.save()
                else:
                    messages.error(request,"Kurs Bulunamadı")
                    return redirect("detailPage")
            else:
                messages.warning(request,"Lütfen giriş yapınız.")
                return redirect("loginPage")
                
        elif submit =="likeSubmit":
            if request.user:
                if kurs_list.exists(): # kurs listesini kontrol et bu formu gönderen bir kurs varmı diye
                    kurs =kurs_list.first()#first(), bir QuerySet'ten ilk öğeyi (veya belirli bir sıra veya filtreleme kriterine göre ilk öğeyi) almak için kullanılan bir metodudur.

                    kurs.likes += 1
                    kurs.save()
                else:
                    messages.error(request,"Kurs Bulunamadı")
            else:
                messages.warning(request, "Lütfen giriş yapınız.")
                return redirect("loginPage")

        elif submit == "sepetSubmit":
            if request.user:
                if kurs_list.exists():
                    kurs= kurs_list.first()
                    
                    adet = int(request.POST.get("adet"))
                    toplam = adet * float(kurs.price)
                    
                    sepet = Sepet(kurs=kurs, user=request.user, adet=adet, toplam=toplam) 
                    sepet.save()
                    return redirect("sepetPage")
                else:
                    messages.error(request,"Kurs Bulunamadı")
            else:
                messages.warning(request,"Lütfen Giriş Yapınız")
                return redirect("loginPage")
    context = {
        "comment_list":comment_list,
        "kurs_list": kurs_list,
        "kurs_random_list": kurs_random_list[:4],
    }
    return render (request,"detail.html",context)




def indexPage(request):
    kurs_list =Kurs.objects.all()
    kurs_random_list = Kurs.objects.all().order_by("?")
    onlinecategory_list =OnlineCategory.objects.all()
    facetofacecategory_list =FacetoFaceCategory.objects.all()
    province_list = Province.objects.all()
    kurs_comments = Kurs.objects.all().order_by("-comment_num")
    kurs_likes = Kurs.objects.all().order_by("-likes")
    kgelisim = Kurs.objects.filter(onlinecategory__title ="Kişisel Gelişim")  #Bu ksıımda kategorileri tek tek ana sayfamda bellialanlarda gösterebiliyorum
    yazilim = Kurs.objects.filter(onlinecategory__title = "Yazılım") #Bu ksıımda kategorileri tek tek ana sayfamda bellialanlarda gösterebiliyorum
    savunma_sanatlari = Kurs.objects.filter(facetofacecategory__title = "Savunma Sanatları") #Bu ksıımda kategorileri tek tek ana sayfamda bellialanlarda gösterebiliyorum
    
    category_province_options_dict = {}
    for category in facetofacecategory_list:
        category_province_options_dict[category] = category.province_options.all()
        
        
    #count(), Django ORM'de kullanılan bir QuerySet yöntemidir ve bir QuerySet içindeki öğelerin sayısını döndürmek için kullanılır. 
    # Bu metodun kullanımı oldukça basittir ve genellikle veri sayma işlemlerinde kullanılır.
    #annotate fonksiyonu, Django ORM'de kullanılan ve sorgulanan veri kümesini zenginleştirmek için kullanılan bir fonksiyondur. 
    # annotate, QuerySet içindeki her bir öğe için özel hesaplamalar yapmanızı sağlar ve bu hesaplamaları yeni bir alan olarak ekler.
    context = {
        "kurs_list":kurs_list,
        "onlinecategory_list":onlinecategory_list,
        "facetofacecategory_list":facetofacecategory_list,
        "kurs_random_list": kurs_random_list[:8],
        "province_list":province_list,
        "kurs_comments":kurs_comments[:4],
        "kurs_likes":kurs_likes[:4],
        "kgelisim":kgelisim[:4],
        "yazilim":yazilim[:4],
        "savunma_sanatlari":savunma_sanatlari[:4],
        "category_province_options_dict": category_province_options_dict,
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
    else:
        messages.warning(request,"ilgili kurs bulunamadı")
        return redirect("indexPage")

    query = request.GET.get("query")
    print("Arama Sorgusu:", query)
    if query:
        kurs_list = kurs_list.filter(Q(title__icontains=query))
    else:
        messages.warning(request,"ilgili kurs bulunamadı")
        return redirect("indexPage")

        
    
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











