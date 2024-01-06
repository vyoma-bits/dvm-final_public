# In your models.py
from django.db import models
from django.contrib.auth.models import User

class train(models.Model):
    name=models.CharField(max_length=50)
    s1=models.CharField(max_length=250)

    seatsg=models.IntegerField()
    seatss=models.IntegerField()
    seats1=models.IntegerField()
    seats2=models.IntegerField()
    seats3=models.IntegerField()
    time=models.CharField(max_length=20)
    days=models.CharField(max_length=20)
    fareg=models.IntegerField(default=0)
    fares=models.IntegerField(default=0)
    fare1=models.IntegerField(default=0)
    fare2=models.IntegerField(default=0)
    fare3=models.IntegerField(default=0)
    train_id=models.IntegerField()

class passengers(models.Model):
    name=models.CharField(max_length=50)
    train_id=models.CharField(max_length=50)
    mobile=models.CharField(max_length=20,default="0")
    date=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)
    age=models.CharField(max_length=30)
    meal=models.CharField(max_length=30)
    unique_id=models.CharField(max_length=34)
    s1=models.CharField(max_length=34)
    s2=models.CharField(max_length=34)
    clas=models.CharField(max_length=78)
    fare=models.IntegerField(default=0)
   


class wallet(models.Model):
    name=models.CharField(max_length=50)
    amount=models.IntegerField(default=0)
class info(models.Model):
    name=models.CharField(max_length=50)
    id_1=models.IntegerField()
    date=models.CharField(max_length=20)
    seatsg=models.IntegerField()
    seatss=models.IntegerField()
    seats1=models.IntegerField()
    seats2=models.IntegerField()
    seats3=models.IntegerField()
    time=models.CharField(max_length=50)

    s_1=models.CharField(max_length=250)

    fareg=models.IntegerField(default=0)
    fares=models.IntegerField(default=0)
    fare1=models.IntegerField(default=0)
    fare2=models.IntegerField(default=0)
    fare3=models.IntegerField(default=0)
class user1(models.Model):
    user=models.CharField(max_length=50)
    unique_id=models.CharField(max_length=50)
   
class journeys(models.Model):
    id1=models.CharField(max_length=50)
    journey=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    date=models.CharField(max_length=50)
    time=models.CharField(max_length=50)
    user=models.CharField(max_length=70)





    
