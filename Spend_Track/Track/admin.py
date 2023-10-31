from django.contrib import admin

# Register your models here.
from Track.models import *


admin.site.register(TrackRecord)
admin.site.register(CreditCard)
admin.site.register(TrackType)
