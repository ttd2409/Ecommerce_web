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
    order = None
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
    context ={}
    return render(request,'app/checkout.html',context)
    

