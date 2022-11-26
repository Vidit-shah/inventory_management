from django import forms

from .models import Invoice

class InvoiceForm(forms.ModelForm):
	class Meta:
		model = Invoice
		line_two_discount = forms.IntegerField(widget = forms.NumberInput(attrs={'class':'form-control','placeholder':25,'onkeyup':'totalSum()','id': 'latcentre1'}))
		# exclude = ('line_two_total_price',)

		# fields = ['name', 'phone_number', 'invoice_date','address', 'invoice_number',
		# 		'line_two', 'line_two_quantity','line_two_serial', 'line_two_HSN', 'line_two_unit_price', 'line_two_discount', 'line_two_total_price',
		# 		'line_three', 'line_three_quantity','line_three_serial', 'line_three_HSN', 'line_three_unit_price', 'line_three_discount', 'line_three_total_price',
		# 		'line_four', 'line_four_quantity','line_four_serial', 'line_four_HSN', 'line_four_unit_price', 'line_four_discount', 'line_four_total_price', 
		# 		'total', 'subtotal', 'paid', 'invoice_type', 'cgst','cgst_value','sgst', 'sgst_value','balance'
		# 		]
		
		
		fields = ['name', 'phone_number', 'invoice_date','address', 'invoice_number',
						'line_two', 'line_two_quantity','line_two_serial', 'line_two_HSN', 'line_two_unit_price', 'line_two_discount', 'line_two_total_price'	
						]
		# fields = ['line_two_discount']
		# 'line_two_total_price':forms.NumberInput(attrs={'class':'form-control','placeholder':'quantity','onkeyup':'totalSum()'})



class InvoiceUpdateForm(forms.ModelForm):
	class Meta:
		model = Invoice
		fields = ['name', 'phone_number', 'invoice_date','address', 'invoice_number',
				'line_two', 'line_two_quantity','line_two_serial', 'line_two_HSN', 'line_two_unit_price', 'line_two_discount', 'line_two_total_price',
				'line_three', 'line_three_quantity','line_three_serial', 'line_three_HSN', 'line_three_unit_price', 'line_three_discount', 'line_three_total_price',
				'line_four', 'line_four_quantity','line_four_serial', 'line_four_HSN', 'line_four_unit_price', 'line_four_discount', 'line_four_total_price', 
				'total', 'subtotal', 'paid', 'invoice_type', 'cgst','cgst_value','sgst', 'sgst_value','balance'
				]
                