from django.db import models

# Create your models here.
class Register(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    mobilenumber=models.CharField(max_length=20)
    aadhar=models.CharField(max_length=12)
    password=models.CharField(max_length=30)
class Donate(models.Model):
    username=models.CharField(max_length=100)
    mobilenumber=models.CharField(max_length=20)
    product=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    quantity=models.IntegerField()
    quality=models.CharField(max_length=5)
    desc=models.CharField(max_length=300)
class Requests(models.Model):
    username=models.CharField(max_length=100)
    item=models.CharField(max_length=100)
    quantity=models.IntegerField()
    address=models.CharField(max_length=300)
class Count(models.Model):
    itemname=models.CharField(max_length=100)
    requestcount=models.IntegerField()
    donatedcount=models.IntegerField()
    
