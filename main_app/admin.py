from django.contrib import admin
from .models import Customer
from .models import Menu
from .models import Order

# Register your models here.

admin.site.register(Customer)
admin.site.register(Menu)
admin.site.register(Order)