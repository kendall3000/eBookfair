from django.contrib import admin
import models.models as m

# Register your models here.
@admin.register(m.Product)
class ProductAdmin(admin.ModelAdmin):
    pass