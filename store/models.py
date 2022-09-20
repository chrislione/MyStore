from audioop import maxpp
import email
from turtle import mode
from django.db import models

# Create your models here.
# class Product(models.model):
#     title=models.CharField(max_length=255) #( Note this is required)
#     description=models.TextField()
#     price=models.DecimalField(max_digits=6, decimal_places=2)#(25555.99 Note this is required)
#     inventory= models.IntegerField()
#     last_update=models.DateTimeField(auto_now=True) # stores the current dateTime everytime this product is updated 

class Customer(models.Model):
    GOLD_MEMBER='G'
    SILVER_MEMBER='S'
    BRONZE_MEMBER='B'
    #field.choices
    MEMBER_SHIP=[
        (GOLD_MEMBER,'GOLD'), 
        (SILVER_MEMBER, 'SILVER'),
        (BRONZE_MEMBER, 'BROZNE'),
    ]
    first_name=models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    email=models.EmailField (unique=True)
    phone=models.CharField(max_length=10)
    birth_date=models.DateField(null=True)
    membership=models.CharField(max_length=1,choices=MEMBER_SHIP,default='B')

# class Order(models.Model):
#     Pending='P'
#     Complete='C'
#     Failed='F'
#     STATUS=[
#         (Pending,'status_pending')
#         (Complete,'status_complete')
#         (Failed,'status_failed')
#     ]
#     placed_at=models.DateTimeField(auto_now=True)
#     payment_status=models.CharField(max_length=1,choice=STATUS,default=Pending)  
# 
#   
#many to many relationship    
class Promotion(models.Model):
    description=models.CharField(max_length=255)
    discount=models.FloatField()
    #product_set: is will returns all the product that a partical promotion is applied to
#------------------------------------------------------------------------------------------------------
class Address(models.Model):
    street=models.CharField(max_length=225)
    city=models.CharField(max_length=255)
    zip=models.CharField(max_length=5, null=True)
    #one to one relatinship
    customer=models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)
    
    #create one to many relationship
    # customer=models.ForeignKey(Customer,on_delete=models.CASCADE)

class Collection(models.Model):
    title=models.CharField(max_length=255)
    featured_product=models.ForeignKey('Product',on_delete=models.SET_NULL,null=True, related_name='+')
    # due to circular dispendency Product class have not yet be seen in the code hence code reads from up to
    # down, we have to put it in a quatation 'Product' to fix the error. Note that if you change the class name 
    # of product to eg Product1 you will have to come back to collection class to change that also
    # also change will get an error due to django is trying to create a path for Collection which is
    # already in Product so related_name but '+'                                  

class Product (models.Model):
    title=models.CharField(max_length=255)
    slug=models.SlugField()# this helps search engine found your search
    #slug will throw in a default value error.fix slug=models.SlugField(null=True)
    #                                                                   (default='-')
    # or do this in a command terminal which will be added but in the 0002_product_slug.py
    discription=models.TextField()
    inventory=models.IntegerField()
    price=models.DecimalField(max_digits=4,decimal_places=2)
    date_update=models.DateField(auto_now_add=True)# store the date the 1st time it was created
    collection=models.ForeignKey(Collection,on_delete=models.PROTECT)  #one to many relationship  
    promotions=models.ManyToManyField(Promotion)

class OrderItem(models.Model):
    PAYMENT_PENDING='P'
    PAYMENT_COMPLETE='C'
    PAYMENT_FAILED='F'

    ORD_STATUS=[
        (PAYMENT_PENDING,'pending_order'),
        (PAYMENT_COMPLETE,'complete_order'),
        (PAYMENT_FAILED,'failed_order'),

    ]
   
    date_time=models.DateTimeField(auto_now=True)
    order_status=models.CharField(max_length=255,choices=ORD_STATUS,default=PAYMENT_PENDING)
    quantity=models.PositiveSmallIntegerField()
    unit_price=models.DateTimeField()
    
    customer=models.ForeignKey(Customer,on_delete=models.PROTECT)

class Cart(models.Model):
    created_at=models.DateTimeField(auto_now=True)

class CartItems(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE )
    product=models.ForeignKey(Product,on_delete=models.CASCADE )
    quantity=models.PositiveSmallIntegerField()

