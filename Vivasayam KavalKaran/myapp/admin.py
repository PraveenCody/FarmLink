from django.contrib import admin
from .models import Users,Farmer,AllProducts

# Register your models here.
admin.site.register(Farmer)
admin.site.register(Users)
admin.site.register(AllProducts)