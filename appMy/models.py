from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title =models.CharField(("Başlik"), max_length=50)
    alt_title1 = models.CharField(("Alt Başlık1"), max_length=50, null =True, blank = True)
    alt_title2 = models.CharField(("Alt Başlık2"), max_length=50, null =True, blank = True)
    alt_title3 = models.CharField(("Alt Başlık3"), max_length=50, null =True, blank = True) 
    slug = models.SlugField(("Slug"))
    
    def __str__(self):
        return self.title
    
class Kurs(models.Model):
    user = models.ForeignKey(User, related_name = "user1", verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name=("Kategori"), null =True, on_delete=models.CASCADE)
    title = models.CharField(("Başlik"), max_length=50)
    puan = models.IntegerField(("Puan"), default=0)
    price = models.IntegerField(("Fiyat"), default=0)
    image = models.ImageField(("Resim"), upload_to="kurs",)    
    
    def __str__(self):
        return self.title
