from django.db import models
from CustomUser.models import CustomUser

# Create your models here.

class CreditCard(models.Model):
    User_Email = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    CreditCard_Name = models.TextField(max_length=50)
    CreditCard_Detail = models.TextField(max_length=100)
    CreditCard_PayDate = models.DateField(blank=True, default='')

class TrackType(models.Model):
    User_Email = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    Spend_Type = models.TextField(max_length=50)

class TrackRecord(models.Model):
    Track_ID = models.AutoField(verbose_name='TrackID', primary_key=True)
    User_Email = models.ForeignKey(to=CustomUser, verbose_name='CustomUser', on_delete=models.CASCADE)
    Track_Type = models.ForeignKey(to=TrackType, verbose_name='TrackType', on_delete=models.CASCADE)
    Credit_Card = models.ForeignKey(to=CreditCard, verbose_name='CreditCard', on_delete=models.CASCADE)
    Track_Amount = models.IntegerField(verbose_name='TrackAmount')
    Track_Detail = models.TextField(verbose_name='TrackDetail', max_length=100)
    Track_Date = models.DateField(verbose_name='TrackDate')