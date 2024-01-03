from django.db import models
from django.contrib.auth.models import User
# from mptt.models import MPTTModel, TreeForeignKey
# from django import forms

class OnlineCategory(models.Model):
    title =models.CharField(("Başlik"), max_length=50)
    yslug = models.SlugField(("Slug"))
    
    def __str__(self):
        return self.title 
class FacetoFaceCategory(models.Model):
    title =models.CharField(("Başlik"), max_length=50)
    tslug = models.SlugField(("Slug"))
    
    def __str__(self):
        return self.title 
    
    
    
    
    
    
    
class Province(models.Model):
    title = models.CharField(max_length=50, null =True)
    islug = models.SlugField(("Slug"),null=True)
    
    
    def __str__(self):
        return self.title    

class Kurs(models.Model):
    user = models.ForeignKey(User, related_name = "user1", verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    onlinecategory = models.ForeignKey(OnlineCategory, verbose_name=("Online Kategori"), blank =True, null =True, on_delete=models.CASCADE)
    facetofacecategory = models.ForeignKey(FacetoFaceCategory, verbose_name=("Yüz Yüze KAtegori"), blank = True, null =True, on_delete=models.CASCADE)
    title = models.CharField(("Başlik"), max_length=50)
    puan = models.IntegerField(("Puan"), default=0)
    price = models.IntegerField(("Fiyat"), default=0)
    image = models.ImageField(("Resim"), upload_to="kurs",)    
    province = models.ForeignKey(Province, verbose_name=("Province"), blank =True, null = True, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
