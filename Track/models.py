from django.db import models
from CustomUser.models import CustomUser
import datetime
# Create your models here.

class CreditCard(models.Model):
    Credit_ID = models.AutoField(verbose_name='CreditID', primary_key=True)
    User_Email = models.ForeignKey(to=CustomUser, related_name="CustomUser_CreditCard", on_delete=models.CASCADE)
    CreditCard_Name = models.CharField(max_length=50, default="Pay in Cash(付現)")
    CreditCard_Detail = models.CharField(max_length=50, default="test")
    CreditCard_PayDate = models.DateField(blank=True, default=datetime.date.today)

    def __str__(self):
        return self.CreditCard_Name

class TrackType(models.Model):
    Type_ID = models.AutoField(verbose_name='TypeID', primary_key=True)
    User_Email = models.ForeignKey(to=CustomUser, related_name="CustomUser_TrackType", on_delete=models.CASCADE)
    Spend_Type = models.CharField(max_length=50, default="Cost of Living(生活費)")

    def __str__(self):
        return self.Spend_Type

class TrackRecord(models.Model):
    Track_ID = models.AutoField(verbose_name='TrackID', primary_key=True)
    User_Email = models.ForeignKey(to=CustomUser, verbose_name='CustomUser',related_name="CustomUser_TrackRecord", on_delete=models.CASCADE)
    Track_Type = models.ForeignKey(to=TrackType, verbose_name='TrackType', on_delete=models.CASCADE)
    # Credit_Card = models.ForeignKey(to=CreditCard, verbose_name='CreditCard', on_delete=models.CASCADE)
    Track_Amount = models.IntegerField(verbose_name='TrackAmount')
    Track_Detail = models.CharField(verbose_name='TrackDetail', max_length=100)
    Track_Date = models.DateField(verbose_name='TrackDate', default=datetime.date.today)
