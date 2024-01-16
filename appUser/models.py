
from django.db import models  
from django.contrib.auth.models import User 
from django.utils.text import slugify # slug ile ilgili tüm kısımları otomatik odldurmamıza yarayan kısım



class Usermy(models.Model):
    user = models.OneToOneField(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    tel = models.CharField(("Telefon"), max_length=50, default = "-")
    address = models.TextField(("Adres"), blank =True)
    profile_image = models.ImageField(("Profil Resmi"), upload_to="profile", max_length=200)
    user_active = models.CharField(("Kullancı Dogrulama Linki"), max_length=50, default=0) # Kullanıcya email aracılı ile link göndermek için kullandıgımız kısım

    def __str__(self):
        return self.user.username

    def save(self):
      print("Usermy model save ====== ")
      super().save() #bu kısım usermyda ki degişikleri kaydetmemzie yarıyor mail göndeririken kullanmamız gerebilir