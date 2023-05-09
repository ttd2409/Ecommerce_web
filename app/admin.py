from django.contrib import admin
from .models import *  #import toan bo model vao 

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Oder)
admin.site.register(Oder_Item)
admin.site.register(Shipping_address)