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







def detailPage(request,kid):
    kurs_list = Kurs.objects.filter(id=kid)
    context = {
        "kurs_list": kurs_list
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


