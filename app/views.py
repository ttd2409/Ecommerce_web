from django.shortcuts import render
from django.http import HttpResponse
from . models import *


# Create your views here.
def home(request):
    products = Product.objects.all() # trỏ tới class lấy toàn bộ đối tượng trong Product
    context = {"products": products}  # chứa những sản phẩm
    return render(request,'app/home.html',context) # đưa view trỏ về home.html context nội dung 

def cart(request):
    items = []
    order = {
        'get_cart_items': 0,
        'get_cart_total': 0,
}
    if request.user.is_authenticated:
        customer = request.user.customer
        order_queryset = Order.objects.filter(customer=customer, complete=False)
        order = order_queryset.first()
        items = order.orderitem_set.all() if order else []
        
    context = {
        'items': items,
        'order': order
    }
    return render(request,'app/cart.html',context)

def checkout(request):
    items = []
    order = {
        'get_cart_items': 0,
        'get_cart_total': 0,
}   
#Nếu người dùng đã đăng nhập,customerđược truy vấn bằng request.user.customerOrder được truy vấn thông qua 
# Order.objects.filter(customer=customer, complete=False)
# lọc những đơn hàng mà khách hàng đang đăng nhập vừa tạo, và xác định rằng đơn hàng chưa hoàn thành.

    if request.user.is_authenticated: # kra người dùng đã đăng nhập hay chưa
        customer = request.user.customer.Order
        order_queryset = Order.objects.filter(customer=customer, complete=False)
        order = order_queryset.first() # truy vấn 
        items = order.orderitem_set.all() if order else [] # lấy tất cả sản phẩm liên quan đến đơn hàng 
        
    context = {
        'items': items,
        'order': order
    }
    return render(request,'app/checkout.html',context)
    

