from django.contrib import admin
from .models import Customer
from .models import Option
from .models import Order

# Register your models here.

admin.site.register(Customer)
admin.site.register(Option)
admin.site.register(Order)
