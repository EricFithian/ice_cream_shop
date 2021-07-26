from django.contrib import admin
from .models import Customer
from .models import Menu_Items
from .models import Order

# Register your models here.

admin.site.register(Customer)
admin.site.register(Menu_Items)
admin.site.register(Order)
