from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.
admin.site.register(Rider)
admin.site.register(Challan)
admin.site.register(Query)
admin.site.register(ChallanImage)
