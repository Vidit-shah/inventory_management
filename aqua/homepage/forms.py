from django import forms
from .models import InventoryItems, InventoryProducts

# forms for Products
class InventoryProductsCreateForm(forms.ModelForm):
    class Meta:
        model = InventoryProducts
        fields = ['product_name', 'product_category', 'product_serial', 'product_HSN',  'product_quantity', 'product_mrp', 'product_dp', 'product_desc', 'product_date']
    
    def clean_product_name(self):
        product_name = self.cleaned_data.get('product_name')
        if not product_name :
            raise forms.ValidationError('This field is Required')
        return product_name   

class InventoryProductsSearchForm(forms.ModelForm):
    class Meta:
        model = InventoryProducts
        fields = ['product_name', 'product_category']

class InventoryProductsUpdateForm(forms.ModelForm):
    class Meta:
        model = InventoryProducts
        fields = ['product_name', 'product_category', 'product_serial', 'product_HSN', 'product_quantity', 'product_mrp', 'product_dp', 'product_desc', 'product_date']
    
    def clean_product_name(self):
        product_name = self.cleaned_data.get('product_name')
        if not product_name :
            raise forms.ValidationError('This field is Required')
        return product_name



# forms for Items
class InventoryItemsCreateForm(forms.ModelForm):
    class Meta:
        model = InventoryItems
        fields = ['item_name', 'item_category', 'item_serial', 'item_HSN', 'item_quantity', 'item_mrp', 'item_dp', 'item_desc', 'item_date']
    
    def clean_product_name(self):
        item_name = self.cleaned_data.get('item_name')
        if not item_name :
            raise forms.ValidationError('This field is Required')
        return item_name

class InventoryItemsUpdateForm(forms.ModelForm):
    class Meta:
        model = InventoryItems
        fields = ['item_name', 'item_category', 'item_serial', 'item_HSN', 'item_quantity', 'item_mrp', 'item_dp', 'item_desc', 'item_date']
    
    def clean_product_name(self):
        product_name = self.cleaned_data.get('item_name')
        if not product_name :
            raise forms.ValidationError('This field is Required')
        return product_name
