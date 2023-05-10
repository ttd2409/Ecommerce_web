from django.shortcuts import render
from django.http import HttpResponse
from . models import *


# Create your views here.
def home(request):
    products = Product.objects.all() # trỏ tới class lấy toàn bộ đối tượng trong Product
    context = {"products": products}  # chứa những sản phẩm
    return render(request,'app/home.html',context) # đưa view trỏ về home.html context nội dung 

def cart(request):
    context ={}
    return render(request,'app/cart.html',context)

def checkout(request):
    context ={}
    return render(request,'app/checkout.html',context)
    
def user(request):
    return render(request,'app/checkout.html')
