# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Category(models.Model):
    cat_id = models.PositiveIntegerField(primary_key=True)
    cat_name = models.CharField(unique=True, max_length=64)

    class Meta:
#        managed = False
        db_table = 'CATEGORY'


class Customer(models.Model):
    cus_id = models.PositiveIntegerField(primary_key=True)
    cus_lname = models.CharField(max_length=45)
    cus_fname = models.CharField(max_length=45)
    cus_initial = models.CharField(max_length=45, blank=True, null=True)
    cus_email = models.CharField(max_length=128)
    cus_phone = models.CharField(max_length=12)
    cus_phone_country = models.CharField(max_length=3)

    class Meta:
#        managed = False
        db_table = 'CUSTOMER'


class Discount(models.Model):
    disc_id = models.PositiveIntegerField(primary_key=True)
    disc_code = models.CharField(max_length=16)
    disc_start = models.DateTimeField()
    disc_end = models.DateTimeField()
    disc_amount = models.DecimalField(max_digits=2, decimal_places=2)

    class Meta:
#        managed = False
        db_table = 'DISCOUNT'


class Images(models.Model):
    img_id = models.PositiveIntegerField(primary_key=True)
    prod = models.ForeignKey('Product', models.DO_NOTHING)
    img_filename = models.CharField(max_length=128)
    img_desc = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
#        managed = False
        db_table = 'IMAGES'


class Invoice(models.Model):
    inv_id = models.PositiveIntegerField(primary_key=True)
    cus = models.ForeignKey(Customer, models.DO_NOTHING)
    inv_date = models.DateTimeField()
    inv_address_line1 = models.CharField(max_length=128)
    inv_address_line2 = models.CharField(max_length=128, blank=True, null=True)
    inv_address_city = models.CharField(max_length=128)
    inv_address_region = models.CharField(max_length=128)
    inv_address_country = models.CharField(max_length=128)
    inv_address_postalcode = models.CharField(max_length=16)

    class Meta:
#        managed = False
        db_table = 'INVOICE'


class Line(models.Model):
    line_id = models.PositiveIntegerField(primary_key=True)
    line_total = models.DecimalField(max_digits=8, decimal_places=2, db_comment='The monetary amount that the items in this line were sold for, after a discount was applied.')
    line_quantity = models.PositiveIntegerField()
    inv = models.ForeignKey(Invoice, models.DO_NOTHING)
    prod = models.ForeignKey('Product', models.DO_NOTHING)
    disc = models.ForeignKey(Discount, models.DO_NOTHING, blank=True, null=True)

    class Meta:
#        managed = False
        db_table = 'LINE'


class Product(models.Model):
    prod_id = models.PositiveIntegerField(primary_key=True)
    prod_name = models.CharField(max_length=128)
    prod_descript = models.CharField(max_length=2048)
    prod_price = models.DecimalField(max_digits=8, decimal_places=2)
    prod_stock = models.PositiveIntegerField()
    cat = models.ForeignKey(Category, models.DO_NOTHING)

    class Meta:
#        managed = False
        db_table = 'PRODUCT'
