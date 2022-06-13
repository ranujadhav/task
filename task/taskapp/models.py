from email.policy import default
from django.db import models

class Register(models.Model):
 username= models.CharField(max_length=200)

 emailid= models.CharField(max_length=200)

 password= models.CharField(max_length=200)

 dob=models.CharField(max_length=200,default=" ")

class Homepage(models.Model):
    sno= models.CharField(max_length=200)
    size= models.CharField(max_length=200)
    prize= models.CharField(max_length=200)
    emi= models.CharField(max_length=200)
