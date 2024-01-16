from django import forms
from appMy.models import Kurs

class KursForm(forms.ModelForm):
    class Meta: # formun özelliklerini belirtmek için kullanırzı meta classını model = Kurs # bu formla ilişkilendirilen modeli belirti
        model = Kurs # Bu kısımda kursu kendine model al 
        fields = ['image', 'title', 'price', 'onlinecategory', 'facetofacecategory', 'province', 'text'] # ve içerisindeki alanları benim için bir  forma dönüşür 



