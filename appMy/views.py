from django.shortcuts import render
# def browsePage(request):
#     context= {}
#     return render(request,"browse.html", context)



def indexPage(request):
    context = {}
    return render(request, "index.html",context)
