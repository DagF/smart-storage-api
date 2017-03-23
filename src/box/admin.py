from django.contrib import admin
from .models import Box, Activity, RFID

admin.site.register(Box)
admin.site.register(RFID)
admin.site.register(Activity)
