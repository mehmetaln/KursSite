from django.shortcuts import render
from appMy.models import *
from django.db.models import Count
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages # kullanıc"
# def browsePage(request):
#     context= {}
#     return render(request,"browse.html", context)



def indexPage(request):
    kurs_list =Kurs.objects.all()
    category_list = Category.objects.all()
    
    context = {
        "kurs_list":kurs_list,
        "category_list":category_list,
    }
    return render(request, "index.html",context)
