from django.contrib import admin
from .models import Project, Product, Combos
# Register your models here.

admin.site.register(Combos)
admin.site.register(Product)