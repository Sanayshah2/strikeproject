from django.contrib import admin

# Register your models here.

from .models import Client
from .models import Order
from .models import Count_table
# from .models import Like


admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Count_table)
