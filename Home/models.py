from django.db import models

# Create your models here.
class classroom_booked(models.Model):
    c_no=models.CharField(max_length=250,default=0)
    name = models.CharField(max_length=250)
    sname = models.CharField(max_length=250)
    time = models.IntegerField()
class feedback(models.Model):
    uname=models.CharField(max_length=250)
    c_no=models.CharField(max_length=250)
    text=models.CharField(max_length=500)
class complaint(models.Model):
    uname=models.CharField(max_length=250)
    c_no=models.CharField(max_length=250)
    text=models.CharField(max_length=500)
    status=models.CharField(max_length=250)
class dt(models.Model):
    c_no=models.CharField(max_length=250,default=0)
    c_date=models.DateField()
    c_time=models.TimeField()
class is_student(models.Model):
    username=models.CharField(max_length=250)
    student=models.CharField(max_length=250)