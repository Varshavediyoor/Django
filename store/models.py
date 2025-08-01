from email.policy import default
from tkinter.constants import CASCADE

from django.db import models
from django.contrib.auth.models import User
import datetime
import os


def get_file_path(request,filename):
    original_filename=filename
    nowTime=datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename='%s%s' % (nowTime,original_filename)
    return os.path.join('uploads/',filename)

class Category(models.Model):
    slug=models.CharField(max_length=50,null=False,blank=False)
    name=models.CharField(max_length=50,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path,null=False,blank=False)
    description=models.TextField(max_length=150,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0=default,1=Hidden")
    trending=models.BooleanField(default=False,help_text="0=default,1=Trending")
    meta_title=models.CharField(max_length=100,null=False,blank=False)
    meta_keyword=models.CharField(max_length=100,null=False,blank=False)
    meta_description=models.TextField(max_length=50,null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=50, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    product_image = models.ImageField(upload_to=get_file_path, null=False, blank=False)
    small_description=models.CharField(max_length=150,null=False,blank=False)
    quantity=models.IntegerField(null=False,blank=False)
    description = models.TextField(max_length=150, null=False, blank=False,default="no Available")
    original_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0=default,1=Hidden")
    trending=models.BooleanField(default=False,help_text="0=default,1=Trending")
    tag=models.CharField(max_length=100,null=False,blank=False)
    meta_title = models.CharField(max_length=100, null=False, blank=False)
    meta_keyword = models.CharField(max_length=100, null=False, blank=False)
    meta_description = models.TextField(max_length=50, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    product_qty=models.IntegerField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)


class Wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now=True)

from django.db import models
from django.contrib.auth.models import User

# Order Model
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=100, null=False)
    lname = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=100, null=False)
    address = models.TextField(null=False)
    city = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=100, null=False)
    country = models.CharField(max_length=100, null=False)
    pincode = models.CharField(max_length=50, null=False)
    total_price = models.FloatField(null=False)
    payment_mode = models.CharField(max_length=50, null=False)
    payment_id = models.CharField(max_length=100, null=False)

    ORDER_STATUS = (
        ("pending", "pending"),
        ("out for shipping", "out for shipping"),
        ("completed", "completed"),
    )

    status = models.CharField(max_length=50, choices=ORDER_STATUS, default="pending")
    messages = models.TextField(null=False)
    tracking_no = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return f'{self.id} - {self.tracking_no}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)

    def _str_(self):
        return f'{self.order.tracking_no}'

# Profile Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50, null=False)
    address = models.TextField(null=False)
    city = models.CharField(max_length=50, null=False)
    state = models.CharField(max_length=50, null=False)
    country = models.CharField(max_length=100, null=False)
    pincode = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.user.name