from django.contrib import admin

# Register your models here.
from Track.models import *

class TrackRecordAdmin(admin.ModelAdmin):
    list_display = ('Track_ID', 'User_Email', 'Track_Type', 'Track_Amount', 'Track_Detail', 'Track_Date')

class TrackTypeAdmin(admin.ModelAdmin):
    list_display = ('Type_ID', 'User_Email', 'Spend_Type')

admin.site.register(TrackRecord, TrackRecordAdmin)
# admin.site.register(CreditCard)
admin.site.register(TrackType, TrackTypeAdmin)
