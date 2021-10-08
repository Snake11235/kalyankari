# Create your models here.
from django.db import models


class Notices(models.Model):
    Notice_Name = models.CharField(max_length=50)
    Notice_Content = models.TextField(max_length=100)
    Notice_Status = models.BooleanField(default=False)


class Slider(models.Model):
    Slider_Name = models.CharField(max_length=50)
    Slider_Path = models.ImageField(max_length=200)
    Slider_Status = models.BooleanField(default=False)
    Slide_Message = models.TextField(max_length=100)


class InstitutionalProfile(models.Model):
    Institutional_Capital = models.IntegerField()
    Institutional_Assets = models.IntegerField()
    Institutional_Deposits = models.IntegerField()
    Institutional_Members = models.IntegerField()
    Institutional_Reserve_Fund = models.IntegerField()


class Services(models.Model):
    Services_Name = models.CharField(max_length=50)
    Services_Status = models.BooleanField(default=False)
    Services_Message = models.TextField(max_length=100)


class Branch(models.Model):
    Branch_Name = models.CharField(max_length=100)
    Branch_Path = models.ImageField(max_length=200)
    Branch_Status = models.BooleanField(default=False)
    Branch_Message = models.TextField(max_length=100)
    Branch_Address = models.CharField(max_length=100)
    Branch_Contact1 = models.CharField(max_length=20)
    Branch_Contact2 = models.CharField(max_length=20, blank=True)



class Saving(models.Model):
    Saving_Name = models.CharField(max_length=30)
    Saving_Status = models.BooleanField(default=False)
    Saving_Message = models.TextField(max_length=100)
    Saving_Intrestrate = models.CharField(max_length=20)
    Saving_Period = models.CharField(max_length=20)
    Saving_Features = models.TextField(max_length=500)
    Saving_TC = models.TextField(max_length=500)


class Loan(models.Model):
    Loan_Name = models.CharField(max_length=50)
    Loan_Status = models.BooleanField(default=False)
    Loan_Message = models.TextField(max_length=100)
    Loan_Intrestrate = models.CharField(max_length=20)
    Loan_Period = models.CharField(max_length=20)
    Loan_Features = models.TextField(max_length=500)
    Loan_TC = models.TextField(max_length=500)


class ExchangeRate(models.Model):
    Exchange_Name = models.CharField(max_length=50)
    Exchange_Status = models.BooleanField(default=False)
    Exchange_Message = models.TextField(max_length=100)


class SuccessStory(models.Model):
    Name = models.CharField(max_length=50)
    Status = models.BooleanField(default=False)
    Message = models.TextField(max_length=100)
