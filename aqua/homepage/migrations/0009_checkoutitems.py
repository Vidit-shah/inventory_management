# Generated by Django 4.1.2 on 2022-10-31 09:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0008_checkout_cost_cgst_checkout_cost_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckoutItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costi_name', models.CharField(max_length=50)),
                ('costi_address', models.CharField(max_length=100)),
                ('costi_number', models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)])),
                ('discounti', models.FloatField(default='0.00', max_length=10)),
                ('costi_cgst', models.FloatField(default='0.00', max_length=10)),
                ('costi_sgst', models.FloatField(default='0.00', max_length=10)),
                ('costi_date', models.DateTimeField()),
                ('export_to_csv', models.BooleanField(default=True)),
            ],
        ),
    ]
