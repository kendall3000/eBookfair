# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * [Done - CT] Rearrange models' order
#   * [Done - CT] Make sure each model has one field with primary_key=True
#   * [Done - CT] Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * [Done - CT] Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Category(models.Model):
    #cat_id = models.AutoField(primary_key=True)
    cat_id = models.PositiveIntegerField(primary_key=True)
    cat_name = models.CharField(unique=True, max_length=64)

    class Meta:
        db_table = 'CATEGORY'


class Customer(models.Model):
    #cus_id = models.AutoField(primary_key=True)
    cus_id = models.PositiveIntegerField(primary_key=True)
    cus_lname = models.CharField(max_length=45)
    cus_fname = models.CharField(max_length=45)
    cus_initial = models.CharField(max_length=45, blank=True, null=True)
    cus_email = models.CharField(max_length=128)
    cus_phone = models.CharField(max_length=12)
    cus_phone_country = models.CharField(max_length=3)

    class Meta:
        db_table = 'CUSTOMER'


class Discount(models.Model):
    #disc_id = models.AutoField(primary_key=True)
    disc_id = models.PositiveIntegerField(primary_key=True)
    disc_code = models.CharField(max_length=16)
    disc_start = models.DateTimeField()
    disc_end = models.DateTimeField()
    disc_amount = models.DecimalField(max_digits=2, decimal_places=2)

    class Meta:
        db_table = 'DISCOUNT'


class Invoice(models.Model):
    #inv_id = models.AutoField(primary_key=True)
    inv_id = models.PositiveIntegerField(primary_key=True)
    cus = models.ForeignKey(Customer, on_delete=models.CASCADE)
    inv_date = models.DateTimeField()
    inv_address_line1 = models.CharField(max_length=128)
    inv_address_line2 = models.CharField(max_length=128, blank=True, null=True)
    inv_address_city = models.CharField(max_length=128)
    inv_address_region = models.CharField(max_length=128)
    inv_address_country = models.CharField(max_length=128)
    inv_address_postalcode = models.CharField(max_length=16)

    class Meta:
        db_table = 'INVOICE'


class Product(models.Model):
    #prod_id = models.AutoField(primary_key=True)
    prod_id = models.PositiveIntegerField(primary_key=True)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    prod_name = models.CharField(max_length=128)
    prod_descript = models.CharField(max_length=2048)
    prod_price = models.DecimalField(max_digits=8, decimal_places=2)
    prod_stock = models.PositiveIntegerField()

    class Meta:
        db_table = 'PRODUCT'


class Images(models.Model):
    #img_id = models.PositiveIntegerField()
    img_id = models.PositiveIntegerField(primary_key=True)
    #prod = models.OneToOneField('Product', on_delete=models.CASCADE, primary_key=True)  # The composite primary key (prod_id, img_id) found, that is not supported. The first column is selected.
    prod = models.ForeignKey('Product', on_delete=models.CASCADE)
    
    img_filename = models.CharField(max_length=128)
    img_desc = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        db_table = 'IMAGES'
        #unique_together = (('prod', 'img_id'),)
        unique_together = (('inv_id', 'prod'),)


class Line(models.Model):
    #line_id = models.PositiveIntegerField(unique=True)
    line_id = models.PositiveIntegerField(unique=True, primary_key=True)
    #inv = models.OneToOneField(Invoice, on_delete=models.CASCADE, primary_key=True)  # The composite primary key (inv_id, line_id) found, that is not supported. The first column is selected.
    inv = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    
    prod = models.ForeignKey('Product', on_delete=models.CASCADE)
    disc = models.ForeignKey(Discount, on_delete=models.CASCADE, blank=True, null=True)
    line_quantity = models.PositiveIntegerField()
    line_total = models.DecimalField(max_digits=8, decimal_places=2, db_comment='The monetary amount that the items in this line were sold for, after a discount was applied.')

    class Meta:
        db_table = 'LINE'
        #unique_together = (('inv', 'line_id'),)
        unique_together = (('line_id', 'inv'),)
