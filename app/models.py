from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# tạo các bảng cơ sở dữ liệu
class Customer(models.Model):
    # name customer
    user = models.OneToOneField(User, on_delete = models.SET_NULL, null= True, blank= False)
    name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    # name product
    name = models.CharField(max_length= 255, null= True) 
    price = models.FloatField()
    digital = models.BooleanField(default=False, null = True, blank = False) # ktra sản phẩm có phải kĩ thuật số không 
    image = models.ImageField(null= True, blank= True)
    
    def __str__(self):
        return self.name
    
    @property # điều chỉnh thuộc tính trong class
    # lấy url của image
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete= models.SET_NULL, blank= True, null= True)
    date_order = models.DateTimeField(auto_now_add= True)
    complete = models.BooleanField(default=False, null= True, blank= False)
    transaction_id = models.CharField(max_length= 255, null= True)
    
    def __str__(self):
        return str(self.id)

    # số lượng giỏ hàng
    @property
    def get_cart_items(self):
        oderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in oderitems])
        return total
    # tính tổng tiền
    @property
    def get_cart_total(self):
        oderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in oderitems])
        return total
        

# customer oder items
class Orderitem(models.Model):
    product = models.ForeignKey(Product, on_delete= models.SET_NULL, blank= True, null= True)
    order = models.ForeignKey(Order, on_delete= models.SET_NULL, blank= True, null= True)
    quantity = models.IntegerField(default= 0, null= True, blank= True)
    date_added = models.DateTimeField(auto_now_add= True)
    # tổng tiền
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class Shipping_address(models.Model):
    customer = models.ForeignKey(Customer, on_delete= models.SET_NULL, blank= True, null= True)
    order = models.ForeignKey(Order, on_delete= models.SET_NULL, blank= True, null= True)
    address = models.CharField(max_length= 200,null= True)
    city = models.CharField(max_length= 200,null= True)
    state = models.CharField(max_length= 200,null= True)
    mobile = models.CharField(max_length= 10,null= True)
    date_added = models.DateTimeField(auto_now_add= True)
    
    def __str__(self):
        return self.address