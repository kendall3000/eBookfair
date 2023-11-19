from django.contrib import admin
import models.models as m

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass