from django.contrib import admin
from .forms import InventoryProductsCreateForm, InventoryItemsCreateForm

# Register your models here.
from .models import InventoryProducts
from .models import InventoryItems

class InventoryProductsCreateAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_category', 'product_serial', 'product_HSN',  'product_quantity', 'product_mrp', 'product_dp', 'product_desc', 'product_date']
    form = InventoryProductsCreateForm
    list_filter = ['product_category']
    search_fields = ['product_name', 'product_category' ]

class InventoryItemsCreateAdmin(admin.ModelAdmin):
    list_display = ['item_name', 'item_category', 'item_serial', 'item_HSN',  'item_quantity', 'item_mrp', 'item_dp', 'item_desc', 'item_date']
    form = InventoryItemsCreateForm
    list_filter = ['item_category']
    search_fields = ['item_name', 'item_category' ]


admin.site.register(InventoryProducts, InventoryProductsCreateAdmin)
admin.site.register(InventoryItems, InventoryItemsCreateAdmin)
