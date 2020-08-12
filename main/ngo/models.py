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