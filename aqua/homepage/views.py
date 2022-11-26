from django.shortcuts import render,HttpResponse, redirect
from .models import * 

from .forms import InventoryProductsCreateForm, InventoryProductsUpdateForm
from .forms import InventoryItemsCreateForm, InventoryItemsUpdateForm
from purchase.forms import InvoiceForm, InvoiceUpdateForm
from purchase.models import *

# Create your views here.
def index(request):
    total_invoices = Invoice.objects.count()
    queryset = Invoice.objects.order_by('-invoice_date')[:6]
    context = {
		"total_invoices": total_invoices,
		"queryset": queryset,
	}
    return render(request,'index.html',context)
    
def about(request):
    return HttpResponse('This is about page')


# Pages for Login & Signup:
def login(request):
    return render(request, 'login.html')    

def signup(request):
    return render(request, 'signup.html')


# Pages for list,adding,deleting the products:
def products(request):
    title = 'Product List'
    queryset = InventoryProducts.objects.all()
    context = {
        'title': title,
        'queryset' : queryset,
    }

    return render(request, 'inventory/product.html', context)

def add_products(request):
    form = InventoryProductsCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/products')

    context = {
        "form" : form,
        "title" : "Add Products",
    }
    return render(request, 'inventory/add_products.html', context)

def update_products(request, pk):
    queryset = InventoryProducts.objects.get(id=pk)
    form = InventoryProductsUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = InventoryProductsUpdateForm(request.POST, instance=queryset)
    
    if form.is_valid():
        form.save()
        return redirect('/products')

    context = {
        "form" : form,
    }
    return render(request, 'inventory/add_products.html', context)

def delete_products(request, pk):
    queryset = InventoryProducts.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('/products')
    return render(request, 'inventory/delete_product.html')



# Pages for list,adding,deleting the items:
def items(request):
    title = 'Items List'
    queryset = InventoryItems.objects.all()
    context = {
        'title': title,
        'queryset' : queryset,
    }
    return render(request, 'inventory/item.html',context)

def add_items(request):
    form = InventoryItemsCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/items')

    context = {
        "form" : form,
        "title" : "Add Products",
    }
    return render(request, 'inventory/add_item.html', context)

def update_item(request, pk):
    queryset = InventoryItems.objects.get(id=pk)
    form = InventoryItemsUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = InventoryItemsUpdateForm(request.POST, instance=queryset)
    
    if form.is_valid():
        form.save()
        return redirect('/items')

    context = {
        "form" : form,
    }

    return render(request, 'inventory/add_item.html', context)

def delete_item(request, pk):
    queryset = InventoryItems.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('/items')
    return render(request, 'inventory/delete_item.html')


# Pages for checkout the products:
def productCheckout(request):
    title = 'This is checkout page'
    queryset = Invoice.objects.all()
    context = {
        'title' : title,
        'queryset':queryset
    }
    return render(request,'checkout/checkout_product.html',context)

def add_productCheckout(request):
    form = InvoiceForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~ TESTING ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 

        # Does the Calculations for the final product
        instance.line_two_total_price = instance.line_two_unit_price - ((instance.line_two_unit_price)*instance.line_two_discount/100)
        instance.save()
        form.save()
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~ TESTING ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 

        return redirect('/productCheckout')
    context = {
        'form': form
        }
        
     #   add_prodCheck is the new html page with simplified code lines
    return render(request,'checkout/add_prodCheck.html', context)

def update_productInvoice(request, pk):
	queryset = Invoice.objects.get(id=pk)
	form = InvoiceUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = InvoiceUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('/productCheckout')

	context = {
		'form':form
	}
	return render(request, 'checkout/add_productCheckout.html', context)

def delete_productInvoice(request, pk):
	queryset = Invoice.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('/productCheckout')
	return render(request, 'checkout/delete_productInvoice.html')

