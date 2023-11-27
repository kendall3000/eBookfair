from django.contrib import admin
import BookFair.models as m

@admin.register(m.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["prod_id", "prod_name"]

@admin.register(m.Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ["disc_id", "disc_code", "disc_start", "disc_end", "disc_amount"]

@admin.register(m.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["cat_id", "cat_name"]

@admin.register(m.Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ["inv_id", "inv_date"]

@admin.register(m.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["cus_email"]