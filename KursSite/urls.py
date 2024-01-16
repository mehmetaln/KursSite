"""
URL configuration for KursSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appMy.views import *
from appUser.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexPage, name="indexPage"),
    path('all/', allkursPage, name = "allkursPage"),
    path('all/o/<oslug>', allkursPage, name = "allkursPage2"),
    path('all/i/<pslug>', allkursPage, name = "allkursPage3"),
    path('all/f/<fslug>', allkursPage, name = "allkursPage4"),
    path('detail/<kid>', detailPage, name = "detailPage"),
    path('emailPage/', emailPage, name = "emailPage"),
    
    
    
    # USER
    path('login/', loginPage, name="loginPage"),
    path('register/',registerPage, name="registerPage"),
    path('logout/user/',logoutUser,name="logoutUser"),
    path('hesap/',hesapPage, name='hesapPage'),
    
    
    
    
] + static (settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
