
# from random import choices
from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

category_choice = (
    ('Aquaguard','Aquaguard'),
    ('Vaccum Cleaner','Vaccum Cleaner'),
)

class InventoryProducts(models.Model):

    # models for Products.
    product_id = models.AutoField
    product_name = models.CharField(max_length=50,blank=False)
    product_serial = models.CharField(default='',max_length=50,blank=False, unique=True)
    product_HSN = models.CharField(default='0',max_length=50,blank=False)
    product_category = models.CharField(max_length=50,blank=False, choices=category_choice)
    product_mrp = models.FloatField(max_length=10, blank=False)
    product_dp = models.FloatField(max_length=10,blank=False)
    product_quantity = models.IntegerField(default='1',blank=False,validators=[MaxValueValidator(100)])
    product_desc = models.TextField(max_length=100,blank=False)
    product_date = models.DateField()
    export_to_csv = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.product_serial

class InventoryItems(models.Model):

    # models for Items
    item_id = models.AutoField
    item_name = models.CharField(max_length=50,blank=False)
    item_serial = models.CharField(default='',max_length=50,blank=False, unique=True)
    item_HSN = models.CharField(default='0',max_length=50,blank=False)
    item_category = models.CharField(max_length=50,blank=False,choices=category_choice)
    item_mrp = models.FloatField(max_length=10, blank=False)
    item_dp = models.FloatField(max_length=10,blank=False)
    item_quantity = models.IntegerField(default='1',blank=False,validators=[MaxValueValidator(100)])
    item_desc = models.TextField(max_length=100,blank=False)
    item_date = models.DateField()
    export_to_csv = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.item_name

