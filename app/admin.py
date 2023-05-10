from django.contrib import admin
from .models import *  #import toan bo model từ cùng 1 thư mục 

# Register your models here. đăng kí các model đảm bảo chúng hiển thị trong django site cho phép thiết lập và quản lý cơ sở dữ 
# liệu của Django trong trang quản trị.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Orderitem)
admin.site.register(Shipping_address)