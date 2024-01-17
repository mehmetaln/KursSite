from django.contrib import admin
from appMy.models import *
from appUser.models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


admin.site.register(Kurs)
admin.site.register(OnlineCategory)
admin.site.register(FacetoFaceCategory)
admin.site.register(Province)

class UsermyInline(admin.StackedInline):
    model =Usermy
    max_num =1
    can_delete =False
    
class CustomUser(UserAdmin):
    inlines =[UsermyInline,]

admin.site.unregister(User)
admin.site.register(User,CustomUser)
admin.site.register(Comment)
admin.site.register(Like)
    
