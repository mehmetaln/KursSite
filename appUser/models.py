
from django.db import models
from django.contrib.auth.models import User 
from django.utils.text import slugify



class Usermy(models.Model):
    user = models.OneToOneField(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    tel = models.CharField(("Telefon"), max_length=50, default = "-")
    address = models.TextField(("Adres"), blank =True)
    image = models.ImageField(("Profil Resmi"), upload_to="profile", max_length=200)
    # username = models.CharField(("Kullanıcı Adı"), max_length=50)

    def __str__(self):
        return self.user.username
