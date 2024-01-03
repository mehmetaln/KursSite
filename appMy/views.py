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
    kurs_random_list = Kurs.objects.all().order_by("?")
    category_list = Category.objects.all()
    province_list = Province.objects.all()
    
    context = {
        "kurs_list":kurs_list,
        "category_list":category_list,
        "kurs_random_list": kurs_random_list[:8],
        "province_list":province_list
    }
    return render(request, "index.html",context)


def allkursPage(request,cslug =None):
    
    if cslug:
        province_list = Province.objects.filter(province__slug =cslug).order_by('-id')
    else:
        province_list = Province.objects.all().order_by('-id')
    
    
    if cslug:
        kurs_list = Kurs.objects.filter(category__slug = cslug).order_by('-id')
    else:
        kurs_list = Kurs.objects.all().order_by('-id')
        
    query =request.GET.get("query")
    
    if query:
        kurs_list= Kurs.objects.filter(Q(title__icontains = query))    
    
    category_list = Category.objects.all()   # hocaya sorulacak
    
    
    
    
    
    context = {
        "kurs_list":kurs_list,
        "category_list": category_list,

    }
    return render(request,"allkurs.html", context)