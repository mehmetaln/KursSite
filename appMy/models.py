from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# from mptt.models import MPTTModel, TreeForeignKey
# from django import forms
class Province(models.Model):
    title = models.CharField(max_length=50, null =True)
    islug = models.SlugField(("Slug"),null=True)
    
    
    def __str__(self):
        return self.title    
class OnlineCategory(models.Model):
    title =models.CharField(("Başlik"), max_length=50)
    yslug = models.SlugField(("Slug"))
    
    def __str__(self):
        return self.title 
class FacetoFaceCategory(models.Model):
    title =models.CharField(("Başlik"), max_length=50)
    tslug = models.SlugField(("Slug"))
    
    province_options = models.ManyToManyField(Province, verbose_name=("İl Seçenekleri"))
    
    def __str__(self):
        return self.title 
    
    
    
    
    
    
    


class Kurs(models.Model):
    user = models.ForeignKey(User, related_name = "user1", verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    onlinecategory = models.ForeignKey(OnlineCategory, verbose_name=("Online Kategori"), blank =True, null =True, on_delete=models.CASCADE)
    facetofacecategory = models.ForeignKey(FacetoFaceCategory, verbose_name=("Yüz Yüze KAtegori"), blank = True, null =True, on_delete=models.CASCADE)
    title = models.CharField(("Başlik"), max_length=50)
    puan = models.IntegerField(("Puan"), default=0, blank = True)
    price = models.FloatField(("Fiyat"), default=0)
    image = models.ImageField(("Resim"), upload_to="kurs")    
    province = models.ForeignKey(Province, verbose_name=("Province"), blank =True, null = True, on_delete=models.CASCADE)
    text = models.TextField(("Acıklama"), max_length=5000, default = "",)
    comment_num = models.IntegerField(("Yorum Sayısı"), default=0)
    # likes = models.ManyToManyField(User, verbose_name=("Begenen Kullanıcılar"), related_name="user2", blank=True) # userm odeli ile ilşlkilendişriyoruz
    likes = models.IntegerField(("Begeni Sayısı"), default = 0)
    # likes_num = models.IntegerField(("Begeni Sayısı"),default=0)
    
    
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    kurs = models.ForeignKey(Kurs, verbose_name=("Yorum yapılan Kurs"), on_delete=models.CASCADE)
    text = models.CharField(("Yorum"), max_length=50)
    date_now = models.DateTimeField(("Tarih ve Saat"), auto_now_add =True )
    
    def __str__(self):
        return self.kurs.title

class Like(models.Model):
    user= models.ForeignKey(User, verbose_name=("Begenen Kullanci"), on_delete=models.CASCADE)
    kurs = models.ForeignKey(Kurs, verbose_name=("Begenilen Kurs"), on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class Sepet(models.Model):
    kurs = models.ForeignKey(Kurs, verbose_name=("Kurs"), on_delete=models.CASCADE)
    user =models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    adet =models.IntegerField(("Adet"), default = 0)
    toplam = models.FloatField(("Toplam Fiyat"), default =0)
    def __str__(self):
        return self.user.username
    