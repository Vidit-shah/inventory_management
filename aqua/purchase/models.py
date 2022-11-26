from django.db import models

# Create your models here.
class Invoice(models.Model):
	comments = models.TextField(max_length=3000, default='', blank=True, null=True)
	invoice_number = models.IntegerField(blank=True, null=True)
	invoice_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
	name = models.CharField('Customer Name', max_length=120, default='', blank=True, null=True)
	phone_number = models.CharField('Phone number',max_length=120, default='', blank=True, null=True)
	address = models.TextField('Address',max_length=100, default='', blank=True, null=True)

	# input
	line_two = models.CharField('Product 1', max_length=120, default='', blank=True, null=True)
	line_two_quantity = models.IntegerField('Quantity', default=0, blank=True, null=True)
	line_two_serial = models.CharField('Serial no.', max_length=20, default=0, blank=True, null=True)
	line_two_HSN = models.CharField('HSN no.', max_length=20, default=0, blank=True, null=True)
	line_two_unit_price = models.IntegerField('Unit Price', default=0, blank=True, null=True)
	line_two_discount = models.IntegerField(default=0, blank=True, null=True)
	line_two_total_price = models.IntegerField('Line Total ', default=0, blank=True, null=True)

	line_three = models.CharField('Product 2', max_length=120, default='', blank=True, null=True)
	line_three_quantity = models.IntegerField('Quantity', default=0, blank=True, null=True)
	line_three_serial = models.CharField('Serial no.', max_length=20, default=0, blank=True, null=True)
	line_three_HSN = models.CharField('HSN no.', max_length=20, default=0, blank=True, null=True)
	line_three_unit_price = models.IntegerField('Unit Price ', default=0, blank=True, null=True)
	line_three_discount = models.IntegerField(default=0, blank=True, null=True)
	line_three_total_price = models.IntegerField('Line Total', default=0, blank=True, null=True)

	line_four = models.CharField('Product 3', max_length=120, default='', blank=True, null=True)
	line_four_quantity = models.IntegerField('Quantity', default=0, blank=True, null=True)
	line_four_serial = models.CharField('Serial no.', max_length=20, default=0, blank=True, null=True)
	line_four_HSN = models.CharField('HSN no.', max_length=20, default=0, blank=True, null=True)
	line_four_unit_price = models.IntegerField('Unit Price ', default=0, blank=True, null=True)
	line_four_discount = models.IntegerField(default=0, blank=True, null=True)
	line_four_total_price = models.IntegerField('Line Total ', default=0, blank=True, null=True)

	
	cgst = models.FloatField(default=9, blank=True, null=True)
	cgst_value = models.IntegerField(default=0, blank=True, null=True)
	sgst = models.FloatField(default=9, blank=True, null=True)
	sgst_value = models.IntegerField(default=0, blank=True, null=True)
	total = models.IntegerField(default='0', blank=True, null=True)
	subtotal = models.IntegerField(default='0', blank=True, null=True)
	balance = models.IntegerField(default='0', blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	last_updated = models.DateTimeField(auto_now_add=False, auto_now=True, blank=True)
	paid = models.BooleanField(default=False)
	invoice_type_choice = (
			('Invoice with GST', 'Invoice with GST'),
			('Invoice without GST', 'Invoice without GST'),
		)
	invoice_type = models.CharField(max_length=50, default='', blank=True, null=True, choices=invoice_type_choice)

	def __str__(self) -> str:
		return self.invoice_number

	# @property
	# def do_calc(self):
	# 	return 41

	